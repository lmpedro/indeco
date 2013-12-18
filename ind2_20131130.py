# -*- coding: utf-8 -*-

'''
    Este indicador é a idade média dos PROFSSs de cada ecossistema
'''

import time
import json
from conversoes import convertecbo, converteuf, convertecnae, converteescol, convertemicro, convertemeso
import numpy as np
from funcoes_base_inds import *
import os

'''
    Atenção: várias das funções básicas que o programa usa estão descritas, comentadas e definidas no arquivo funcoes_base_inds.py
'''

'''
    Trata-se do programa central. Recebe uma base de dados (com todos os anos), um dicionário que traduz as posições das variáveis entre a base crua e a completa, a identificação em str da dimensão geográfica e o identificador do ecossistema em questão (antes de ser transformado por 'ecotransform(x)'). Retorna um vetor nx1 com os resultados e uma lista com os indíces.
'''

def rodar(bases,defs,geo,neco):
    neconum=ecotransform(neco)
    reduzido=bases[-1]
    geoindex, geoname=geodef(geo)
    
    #ix identifica a posição das variáveis que servirão como controle
    ia=int(defs[geoindex])
    ib=defs[0]
    ic=defs[17]
    id=defs[19]
    
    #criar os conjuntos de valores através dos quais se deve iterar ao calcular as médias. Geram-se listas ordenadas dos valores únicos de uf, cnae... Resume-se a base às observações do ecossistema para restringir o conjunto de cnaes àquelas do ecossistema, e retiram-se observações que não sejam de profss para captar apenas as CBOs dessa categoria.
    seta=uniquevalues(reduzido,ia)
    setc=uniquevalues(reduzido,ic)
    #retirar observações que não são do ecossistema em questão
    reduzidobeta=keepif(reduzido,defs[neconum],1)
    setb=uniquevalues(reduzidobeta,ib)
    #retirar observações que não são de PROFSSs
    reduzido=keepif(reduzido,defs[28],1)
    setd=uniquevalues(reduzido,id)
    
    #obj é a variável objetiva que terá sua média calculada
    obj=defs[21]
    first=[]
    
    '''
        este loop relativamente longo faz o cálculo das estatísticas em questão. Vai-se iterando pelos sets de valores únicos das variáveis de controle anteriormente criadas, gerando, ao final, uma matriz 6d com tuplas de (média, número de ocorrências).
    '''
    
    for index in range(len(bases)):
        reduzido=bases[index]
        
        #retira-se observações que não sejam do ecossistema em questão ou de profss
        reduzido=keepif(reduzido,defs[28],1)
        reduzido=keepif(reduzido,defs[neconum],1)
        
        second=[]
        for va in seta:
            intermediary=[]
            for vb in setb:
                theonebeforelast=[]
                for vc in setc:
                    lastinstance=[]
                    for vd in setd:
                        med=media(reduzido,obj,ia,ib,ic,id,va,vb,vc,vd)
                        lastinstance.append(med)
                    theonebeforelast.append(lastinstance)
                intermediary.append(theonebeforelast)
            second.append(intermediary)
        first.append(second)
    
    #criar as listas que servirão de índice aos jsons
    lista_indices=[]
    listia=[]
    for x in seta:
        if geo=='uf': y=converteuf(x)
        if geo=='meso': y=convertemeso(x)
        if geo=='micro': y=convertemicro(x)
        listia.append(y)
    listib=[]
    for x in setb:
        y=convertecnae(x)
        listib.append((x,y))
    listic=[]
    for x in setc:
        y=converteescol(x)
        listic.append(y)
    listid=[]
    for x in setd:
        y=convertecbo(x)
        listid.append((x,y))
    
    lista_indices.append(listia)
    lista_indices.append(listib)
    lista_indices.append(listic)
    lista_indices.append(listid)
    
    vetor= lineariza(first)
    
    return vetor,lista_indices

'''
    Função que cria os jsons para a saída. Recebe um vetor nx1 com os resultados, uma lista com os índices, a dimensão geográfica, o número do ecossistema e o caminho para salvar os jsons. Cria o json e não retorna nada.
'''

def jsoncreate(results,indices,geo,neco,caminho):
    geoindex, geoname=geodef(geo)
    jresults={
        "fonte":"RAIS/MTE (2006-2011)",
        "indicador":[u"Idade média dos PROFSSs","Idade/trabalhador"],
        "estrutura":[
                     "Ano",
                     geoname,
                     "Classificação Nacional de Atividades Econômicas (Classe CNAE)",
                     "Faixa de Escolaridade",
                     "Classificação Brasileira de Ocupações (Família CBO)",
                     "Valores"],
            "indices":[
                       [2006,2007,2008,2009,2010,2011],
                       indices[0],
                       indices[1],
                       indices[2],
                       indices[3],
                       ["Idade média dos PROFSSs","Número de PROFSSs"],
                       ],
                     "valores":list(results),
    }
    #esse if/else garante que o nome dos arquivos terá, na parte que identifica os ecossistemas, dois dígitos
    if neco<10:
        nomearquivo="d_BR"+geo+"020"+str(neco)+".json"
    else: nomearquivo="d_BR"+geo+"02"+str(neco)+".json"
    
    arquivo = open(caminho+nomearquivo,"w")
    arquivo.write(json.dumps(jresults))
    arquivo.close()

'''
    Trata-se da função que efetivamente roda o programa todo. Recebe a dimensão geográfica, o primeiro ecossistema a rodar, o último ecossistema a rodar e um número que identifica qual conjunto de bases usar. Gera todos os jsons a partir dessa combinação, e não retorna nada.
    Quanto à definição das bases,
    0:completa
    1:10%
    2:1%
    3:.25%
    4:.25%, para 2006 e 2007
    5:.25%, para 2006
'''

def ind2(geo='uf',ecoinit=16,ecoend=16,tamanho=5):
    tglobal=time.time()
    print "Começando o programa para o indicador 2..."
    geoindex, geoname=geodef(geo)
    ecoend+=1
    
    #Verifica se o caminho para salvar os jsons existe e, se não, o cria."
    caminho='../Indicadores/Base'+str(tamanho)+'/'
    if os.path.exists(caminho)==False: os.makedirs(caminho)
    
    #definição das bases a serem utilizadas
    if tamanho==0: listabases=['r06.txt','r07.txt','r08.txt','r09.txt','r10.txt','r11.txt']
    if tamanho==1: listabases=['r06s10.txt','r07s10.txt','r08s10.txt','r09s10.txt','r10s10.txt','r11s10.txt']
    if tamanho==2: listabases=['r06s1.txt','r07s1.txt','r08s1.txt','r09s1.txt','r10s1.txt','r11s1.txt']
    if tamanho==3: listabases=['r06s.txt','r07s.txt','r08s.txt','r09s.txt','r10s.txt','r11s.txt']
    if tamanho==4: listabases=['r06s.txt','r07s.txt']
    if tamanho==5: listabases=['r06s.txt']
    if tamanho==6: listabases=['r06.txt']
    if tamanho==7: listabases=['r07.txt']
    if tamanho==8: listabases=['r08.txt']
    if tamanho==9: listabases=['r09.txt']
    if tamanho==10: listabases=['r10.txt']
    if tamanho==11: listabases=['r11.txt']
    
    vars=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,19,21,28,geoindex]
    bases,reduzidodef=arrumabases(listabases,vars)
    
    for neco in range(ecoinit,ecoend):
        teco=time.time()
        results,lista_indices=rodar(bases,reduzidodef,geo,neco)
        jsoncreate(results,lista_indices,geo,neco,caminho)
        teco=round(time.time()-teco,2)
        print "Termina o eco",neco,"em",teco,"s."
    
    tglobal=round((time.time() - tglobal)/60,2)
    print "Tempo total do programa:",tglobal,"min."

'''
    Esta é a lista das variáveis nas bases de dados cruas.
    
    v0   classe_cnae_20
    v1   ecossis_1
    v2   ecossis_10
    v3   ecossis_11
    v4   ecossis_12
    v5   ecossis_13
    v6   ecossis_14
    v7   ecossis_15
    v8   ecossis_16
    v9   ecossis_2
    v10   ecossis_3
    v11   ecossis_4
    v12   ecossis_5
    v13   ecossis_6
    v14   ecossis_7
    v15   ecossis_8
    v16   ecossis_9
    v17   escol_fx
    v18   escolaridade
    v19   familia
    v20   ibss
    v21   idade
    v22   mesorregi
    v23   microrregi
    v24   municipio
    v25   pnivelesp
    v26   pnivelger
    v27   pniveltec
    v28   profss
    v29   sal_dez
    v30   sexo
    v31   sw1
    v32   sw2
    v33   sw3
    v34   tamestab
    v35   uf

'''