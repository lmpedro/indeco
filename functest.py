# -*- coding: utf-8 -*-

'''
    Arquivo para rotinas de testes. Pode ser apagado à vontade.
'''



import time
from conversoes import convertecbo, converteuf, convertecnae, converteescol, convertemicro, convertemeso
import numpy as np
import json
from funcoes_base_inds import *


'''

def jsoncreate(results,indices,geo,neco,caminho):
    geoindex, geoname=geodef(geo)
    jresults={
        "fonte":"RAIS/MTE (2006-2011)",
        "indicador":[u"Proporção de PROFSSs","PROFSSs/trabalhadores(as)"],
        "estrutura":[
                     "Ano",
                     geoname,
                     "Classificação Nacional de Atividades Econômicas (Classe CNAE)",
                     "Faixa de Escolaridade",
                     "Sexo",
                     "Valores"],
        "indices":[
                   [2006,2007,2008,2009,2010,2011],
                   indices[0],
                   indices[1],
                   indices[2],
                   indices[3],
                   ["Proporção de PROFSSs","Número de trabalhadores(as)"],
                   ],
        "valores":list(results),
    }
    #esse if/else garante que o nome dos arquivos terá, na parte que identifica os ecossistemas, dois dígitos
    if neco<10:
        nomearquivo="d_BR"+geo+"030"+str(neco)+".json"
    else: nomearquivo="d_BR"+geo+"03"+str(neco)+".json"
    
    arquivo = open(caminho+nomearquivo,"w")
    arquivo.write(json.dumps(jresults))
    arquivo.close()


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



fonte [0]
indicador [1]
estrutura [5]
indices [5] com mais coisa
nind #

'''

'''
    TEXT!!!    


'''



'''
    Função que cria os jsons para a saída. Recebe o seguinte:
        results: um vetor nx1 com os resultados,
        indices: uma lista de 6 x Xi com os indices. Esta lista deve conter:
            0: os anos
            1-4: os índices das variáveis de corte na ordem em que são iterados
            5: um vetor n x 1 com a descrição das estatísticas calculadas: e.g., [%PROFSS,N trabalhadores]
        geo: a dimensão geográfica, em str
        neco: o número do ecossistema, em int
        caminho: o caminho para salvar os jsons, em str
        fonte: Base de dados utilizada (str)
        indicador: lista em str com o nome do indicador e a unidade de medida: eg, [u"Proporção de PROFSSs","PROFSSs/trabalhadores(as)"]
        estrutura: recebe um vetor 6x1 que indica a estrutura das variáveis que são iteradas (ano, unidade geográfica, CNAE, escolaridade...)
        nind: número do indicador a ser calculado, em int
        
    A função cria o json e não retorna nada.
 
'''

def jsoncreate(results,indices,geo,neco,caminho,fonte,indicador,estrutura,nind):
    geoindex, geoname=geodef(geo)
    jresults={
        "fonte":fonte,
        "indicador":indicador,
        "estrutura":estrutura,
        "indices":indices,
        "valores":list(results),
    }
    #esse if/else garante que o nome dos arquivos terá, na parte que identifica os ecossistemas, dois dígitos
    if neco<10:
        nomearquivo="d_BR"+geo+"0"+str(nind)+"0"+str(neco)+".json"
    else: nomearquivo="d_BR"+geo+"0"+str(nind)+str(neco)+".json"
    
    arquivo = open(caminho+nomearquivo,"w")
    arquivo.write(json.dumps(jresults))
    arquivo.close()

'''
   onlyprofss: list com dois elementos. O primeiro indica se o cálculo deverá excluir os profss da base de dados (==1) ou não (==0), o segundo indica a posição da variável profss na base de dados.
   sets: lista com quatro elementos, cada um deles um set dos valores únicos pelos quais se deve iterar as variáveis de controle
   obj: posição da variável objetiva na base de dados
   controls: lista com cinco ints que indicam a posição da variável objetiva [0] e das variáveis de controle [1-4] na base de dados
   neconum: posição na base de dados da variável que indica se a observação em questão pertence ao ecossistema para o qual se calcula
   retorna o vetor nx1 com os resultados calculados
'''

def calculo(bases,onlyprofss,sets,controls,neconum):
    first=[]
    for index in range(len(bases)):
        reduzido=bases[index]
        
        #retira-se observações que não sejam de profss
        assert onlyprofss[0]==0 or onlyprofss[0]==1
        if onlyprofss[0]==1:
            reduzido=keepif(reduzido,onlyprofss[1],1)
        #retira-se observações que não sejam do ecossistema em questão
        reduzido=keepif(reduzido,neconum,1)
        
        second=[]
        for va in sets[0]:
            intermediary=[]
            for vb in sets[1]:
                theonebeforelast=[]
                for vc in sets[2]:
                    lastinstance=[]
                    for vd in sets[3]:
                        med=media(reduzido,controls[0],controls[1],controls[2],controls[3],controls[4],va,vb,vc,vd)
                        lastinstance.append(med)
                    theonebeforelast.append(lastinstance)
                intermediary.append(theonebeforelast)
            second.append(intermediary)
        first.append(second)
    
    vetor=lineariza(first)
    return vetor

def listas():
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

def basesdef(tamanho):
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
    return listabases

