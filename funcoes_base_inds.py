# -*- coding: utf-8 -*-

'''
    Este arquivo contém várias funções básicas que serão utilizadas por uma multiplicidades de indicadores. Ficam todas aqui para facilitar sua manutenção.
'''


import argparse
import time
from conversoes import convertecbo, converteuf, convertecnae, converteescol, convertemicro, convertemeso
import numpy as np
import json
import os


'''
carregabase recebe o nome de um arquivo, carrega ele como uma lista e retorna esta, para ser usada como base de dados. Há uma rotina para identificar se dada variável é int, float ou str.
'''


def carregabase(entrada):
    caminhobase='/Users/pedro/CTI/Python/Bases/'
    linhas=open(caminhobase+entrada,'r')
    
    pronto= []
    for linha in linhas:
        lista = linha.split(";")
        for x in range(len(lista)):
            lista[x]=lista[x].replace('\r\n','')
            lista[x]=lista[x].replace('\"','')
            if lista[x]=='.': lista[x]=None
            if lista[x]=='': lista[x]=None
            if lista[x]=='\n': lista[x]=None
            if isinstance(lista[x],str):
                try:
                    lista[x]=float(lista[x])
                    if lista[x]==int(lista[x]): lista[x]=int(lista[x])
                except ValueError:
                    pass
        if len(lista)>1: pronto.append(lista)
    linhas.close
    return pronto

'''
keepvar recebe uma base de dados e uma lista com o índice [0,1....n] das variáveis que se quer manter. retorna a base de dados mantidas apenas as variáveis especificadas na entrada. Retorna também um dicionário 'vardef' que tem como chaves os índices das variáveis mantidas na base anterior e, associados a essas chaves, o índice dessas variáveis na nova base. Exemplo: uma base de entrada com dez variáveis, escolhe-se manter as vars 0 e 9; a saída terá duas vars, e e vardef={0:0,9:1}.
'''

def keepvar(entrada,vars):
    vars.sort()
    temptot, vardef=[],{}
    for i in range(len(entrada)):
        templine=[]
        for j in range(len(entrada[0])):
            for x in vars:
                if j==x:
                    templine.append(entrada[i][j])
        temptot.append(templine)
    for x in range(len(vars)):
        vardef[vars[x]]=x
    return temptot, vardef

'''
A função media recebe a base de dados (lista) a ser usada, a variável que terá sua média calculada, e quatro pares adicionais de condições: ix identifica a variável de condição de ser investigada e vx o valor que tal variável deve assumir para que dada observação seja incluída na média.
'''

def media(entrada,obj,ia,ib,ic,id,va,vb,vc,vd):
    n,soma=0,0
    for x in entrada:
        if x[ia]==va and x[ib]==vb and x[ic]==vc and x[id]==vd:
            soma+=x[obj]
            n+=1
    try:
        med=[round(float(float(soma)/n),2),n]
    except ZeroDivisionError:
        med=[None,None]
    return med

'''
uniquevalues retorna uma lista ordenada com todos os valores únicos da variável especificada na lista determinada
'''

def uniquevalues(entrada,var):
    tempset=set()
    for x in entrada:
        tempset.add(x[var])
    try: tempset.remove(None)
    except KeyError: pass
    sset=sorted(tempset)
    return sset

'''
keepif deleta todas as observações em que 'var' não é == 'varvalue', e retorna a base de dados reduzida
'''

def keepif(entrada,var,varvalue):
    temp=[]
    for x in entrada:
        if x[var]==varvalue: temp.append(x)
    return temp

'''
fundocalc é uma função que deixou de ser usada. Mas recebe um fundo de escala já existente e uma base de dados (ambas com o mesmo número de variáveis). A partir disso, calcula a menor potência de dez >= que o máximo de cada variável. fundo[j]>=entrada[j], restrito a fundo[j]=10^x (x é inteiro).
'''

def fundocalc(fundo,entrada):
    for j in range(len(entrada)):
        x=fundo[j]
        if entrada[j]=="" or entrada[j]==None: continue
        while x<entrada[j]: x*=10
        fundo[j]=x

'''
uma função estranha, que vem do jeito que o stata organiza as variáveis. serve simplesmente para ficar mais fácil fazer referêrncia ao número do ecossistema em questão
'''

def ecotransform(eco):
    if eco==1: neco=1
    if eco==2: neco=9
    if eco==3: neco=10
    if eco==4: neco=11
    if eco==5: neco=12
    if eco==6: neco=13
    if eco==7: neco=14
    if eco==8: neco=15
    if eco==9: neco=16
    if eco==10: neco=2
    if eco==11: neco=3
    if eco==12: neco=4
    if eco==13: neco=5
    if eco==14: neco=6
    if eco==15: neco=7
    if eco==16: neco=8
    return neco

'''
Essa função recebe uma matriz n-dimensional e retorna um vetor unidimensional. A ordem é determinada pela função flatten do numpy. Ao longo de lineariza, mostra-se o formato da matriz de entrada. Observa-se que é necessário que a matriz seja 'bem formada', isto é, que não tenha dimensões diferentes para diferentes índices superiores (e.g., entrada[0][0] ser um vetor 5x1 e entrada[0][1] ser uma matriz 7x2).
'''

def lineariza(d):
    #a linha abaixo é uma maneira alternativa de mostrar as dimensões da entrada, em seus índices 0. Só é totalmente ajustada para matrizes 6-D, e apenas faz sentido usar em caso de erros.
    #print "Mostrando os vários len(d...)",len(d), len(d[0]), len(d[0][0]), len(d[0][0][0]), len(d[0][0][0][0]), len(d[0][0][0][0][0])
    matriz6d = np.array(d)
    escopo = matriz6d.shape
    print "As dimensões da matriz de entrada são ",escopo
    vetor = matriz6d.flatten()
    print "O vetor de saída tem ",vetor.shape," posições."

    return vetor

'''
geodef recebe uf, meso ou micro como entrada e retorna duas variáveis, uma com o índice da base de dados que contém a variável geográfica em questão e outra com o nome (str) dessa dimensão.
'''

def geodef(geo):
    if geo=='meso':
        indgeo=int(20)
        auxgeo="Mesorregião"
    if geo=='micro':
        indgeo=int(21)
        auxgeo="Microrregião",
    if geo=='uf':
        indgeo=int(33)
        auxgeo="Unidade da Federação"

    return indgeo, auxgeo

'''
Esta função recebe uma lista com o nome dos arquivos que deverão ser agregados para gerar a base de dados completas (com os vários anos) e uma lista com as variáveis que efetivamente serão utilizadas (para remover as demais). Retorna uma variável com a base de dados completas e um dicionário que traduz a posição das variáveis entre a base de dados original (com todas as vars.) e a arrumada.
'''

def arrumabases(listabases,vars):
    tcartotal=time.time()
    bases=[]
    for ano in listabases:
        tcar=time.time()
        dados=carregabase(ano)
        vars.sort()
        #retirar variáveis desnecessárias
        reduzido,reduzidodef=keepvar(dados,vars)
        bases.append(reduzido)
        tcar=round((time.time()-tcar)/60,2)
        print "Carregou ano",ano,"em",tcar,"min."
    tcartotal=round((time.time()-tcartotal)/60,2)
    print "Tempo total de carregar e arrumar bases:",tcartotal,"min."
    return bases,reduzidodef

'''
    Função que cria os jsons para a saída. Recebe o seguinte:
    results: um vetor nx1 com os resultados,
    indices: uma lista de 6 x Xi com os indices. Esta lista deve conter:
    0: os anos
    1-4: os índices das variáveis de corte na ordem em que são iterados
    5: um vetor n x 1 com a descrição das estatísticas calculadas: e.g., [%PROFSS,N trabalhadores]
    geo: a dimensão geográfica, em str
    neco: o número do ecossistema, em int
    tamanho: o tamanho das bases usadas, para colocar os jsons nas pastas corretas
    fonte: Base de dados utilizada (str)
    indicador: lista em str com o nome do indicador e a unidade de medida: eg, [u"Proporção de PROFSSs","PROFSSs/trabalhadores(as)"]
    estrutura: recebe um vetor 6x1 que indica a estrutura das variáveis que são iteradas (ano, unidade geográfica, CNAE, escolaridade...)
    nind: número do indicador a ser calculado, em int
    
    A função cria o json e não retorna nada.
    
'''

def jsoncreate(results,indices,geo,neco,tamanho,fonte,indicador,estrutura,nind):
    geoindex, geoname=geodef(geo)
    jresults={
        "fonte":fonte,
        "indicador":indicador,
        "estrutura":estrutura,
        "indices":indices,
        "valores":list(results),
    }
    
    #Verifica se o caminho para salvar os jsons existe e, se não, o cria."
    caminho='/Users/pedro/CTI/Python/Dashboard/Indicadores/Base'+str(tamanho)+'/'
    if os.path.exists(caminho)==False: os.makedirs(caminho)

    #esse if/else garante que o nome dos arquivos terá, na parte que identifica os ecossistemas, dois dígitos
    if neco<10:
        nomearquivo="d_BR"+geo+"0"+str(nind)+"0"+str(neco)+".json"
    else: nomearquivo="d_BR"+geo+"0"+str(nind)+str(neco)+".json"
    
    arquivo = open(caminho+nomearquivo,"w")
    arquivo.write(json.dumps(jresults))
    arquivo.close()

'''
    Essa função calcula as estatísticas de interesse e retornao um vetor nx1 com os resultados calculados
    base: a base de dados a ser utilizada
    onlyprofss: list com dois elementos. O primeiro indica se o cálculo deverá excluir os profss da base de dados (==1) ou não (==0), o segundo indica a posição da variável profss na base de dados.
    sets: lista com quatro elementos, cada um deles um set dos valores únicos pelos quais se deve iterar as variáveis de controle
    controls: lista com cinco ints que indicam a posição da variável objetiva [0] e das variáveis de controle [1-4] na base de dados
    neconum: posição na base de dados da variável que indica se a observação em questão pertence ao ecossistema para o qual se calcula
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

'''
   Essa função define o nome das bases a serem utilizadas, recebendo como input o tamanho. Retorna uma lista com os caminhos dos arquivos 
'''

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
    if tamanho==12: listabases=['r12.txt']
    if tamanho==13: listabases=['r11s.txt']
    if tamanho==14: listabases=['r10s.txt', 'r11s.txt']
    if tamanho==15: listabases=['r07s.txt','r08s.txt','r09s.txt','r10s.txt','r11s.txt','r12s.txt']
    return listabases

def cmdlparser():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument("-b", "--base", type=int, choices=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], default=5, help="Escolhe a base a ser usada, 0...11    0:completa    1:10perc.    2:1perc.    3:.25perc.    4:.25perc., para 2006 e 2007    5:.25perc., para 2006    6: 2006 inteira    7: 2007 inteira    ...    11: 2011 inteira    ")
    parser.add_argument("-g", "--geo", type=str, choices = ['uf','micro','meso'], default='uf', help="Escolhe a unidade geográfica: uf, micro meso.")
    parser.add_argument("-ei", "--ecoinit", type=int, choices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11,12,13,14,15,16], default='16', help="Escolhe o ecossistema inicial a ser processado: 1...16")
    parser.add_argument("-ee", "--ecoend", type=int, choices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11,12,13,14,15,16], default='16', help="Escolhe o ecossistema final a ser processado: 1...16")
    parser.add_argument("-i", "--ind", type=int, default=1, help="Escolhe o indicador a ser rodado.")

    args = parser.parse_args()
    return args


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