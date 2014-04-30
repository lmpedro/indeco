# -*- coding: utf-8 -*-

'''
    Este indicador é o salário médio dos PROFSSs de cada ecossistema
'''

import time
from conversoes import *
from funcoes_base_inds import *

'''
    Atenção: várias das funções básicas que o programa usa estão descritas, comentadas e definidas no arquivo funcoes_base_inds.py
'''

'''
Trata-se do programa central. Recebe uma base de dados (com todos os anos), um dicionário que traduz as posições das variáveis entre a base crua e a completa, a identificação em str da dimensão geográfica e o identificador do ecossistema em questão (antes de ser transformado por 'ecotransform(x)'). Retorna um vetor nx1 com os resultados e uma lista com os indíces.
'''

def rodar(bases,defs,geo,neco):
    neconum=ecotransform(neco)
    geoindex, geoname=geodef(geo)
    
    #controls: lista com nove ints que indicam a posição da variável objetiva [0], da variável do ecossistema em questão[1], da variável de profss[2], da variável geográfica[3], da variável de cnaes[4], das duas variáveis de controle específicas [5-6] na base de dados, se as duas variáveis de controle devem ser definidas apenas para profss[7] e se o indicador em si é calculado apenas a partir dos PROFSSs [8].
    controls=[
              defs[25],
              defs[neco],
              defs[24],
              int(defs[geoindex]),
              defs[0],
              defs[17],
              defs[18],
              [1,1],
              [1]
              ]
        
    try:
        bases[0,0,0]
        sets=setdef(bases[-1,:,:],controls,neco)
    except IndexError:
        sets=setdef(bases,controls,neco)

    vetor=calculo(bases,sets,controls,neco)

    #criar as listas que servirão de índice aos jsons
    lista_indices=[]
    listanos=[2006,2007,2008,2009,2010,2011]
    lista_indices.append(listanos)
    listia=[]
    for x in sets[0]:
      if geo=='uf': y=converteuf(x)
      if geo=='meso': y=convertemeso(x)
      if geo=='micro': y=convertemicro(x)
      listia.append(y)
    listib=[]
    for x in sets[1]:
      y=convertecnae(x)
      listib.append((x,y))
    listic=[]
    for x in sets[2]:
      y=converteescol(x)
      listic.append(y)
    listid=[]
    for x in sets[3]:
      y=convertecbo(x)
      listid.append((x,y))

    lista_indices.append(listia)
    lista_indices.append(listib)
    lista_indices.append(listic)
    lista_indices.append(listid)
    lista_indices.append(["Salário médio dos PROFSSs","Número de PROFSSs"])
    
    return vetor,lista_indices

'''
    É função final, que roda tudo e cria os jsons. Recebe como argumentos a dimensão geográfica (str), os ecossistemas iniciais e finais para os quais se deve rodar e o tamanho das bases a serem utilizadas. Temos que:
    0:completa
    1:10%
    2:1%
    3:.25%
    4:.25%, para 2006 e 2007
    5:.25%, para 2006
    6: 2006 inteira
    7: 2007 inteira
    ...
    11: 2011 inteira
'''
#geo='uf',ecoinit=16,ecoend=16,tamanho=5
def ind1(geo='uf',ecoinit=16,ecoend=16,tamanho=5):
    args=cmdlparser()
    np.seterr(divide='raise',invalid='raise')
    tglobal=time.time()
    print "Começando o programa para o indicador 1..."
    geoindex, geoname=geodef(geo)
    ecoend+=1
    
    #definição das bases a serem utilizadas
    listabases=basesdef(tamanho)
    
    vars=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,24,25,geoindex]
    bases,reduzidodef=arrumabases(listabases,vars)
    
    fonte=u"RAIS/MTE (2006-2011)"
    indicador=[u"Salário médio dos PROFSSs","R$ correntes/trabalhador"]
    estrutura=[
               "Ano",
               geoname,
               "Classificação Nacional de Atividades Econômicas (Classe CNAE)",
               "Faixa de Escolaridade",
               "Classificação Brasileira de Ocupações (Família CBO)",
               "Valores",
               ]
    nind=1

    for neco in range(ecoinit,ecoend):
       teco=time.time()
       results,lista_indices=rodar(bases,reduzidodef,geo,neco)
       jsoncreate(results,lista_indices,geo,neco,tamanho,fonte,indicador,estrutura,nind)
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
    
    
    0	cnae20classe
    1	ecossis_01
    2	ecossis_02
    3	ecossis_03
    4	ecossis_04
    5	ecossis_05
    6	ecossis_06
    7	ecossis_07
    8	ecossis_08
    9	ecossis_09
    10	ecossis_10
    11	ecossis_11
    12	ecossis_12
    13	ecossis_13
    14	ecossis_14
    15	ecossis_15
    16	ecossis_16
    17	escol_fx
    18	familia
    19	idade
    20	mesorregi
    21	microrregi
    22	municipio
    23	pnivel
    24	profss
    25	sal_dez
    26	sexo
    27	swfx
    28	tamestab
    29	uf

'''