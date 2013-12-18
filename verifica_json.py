# -*- coding: utf-8 -*-

import time
import json
import numpy as np

def carrega_json(entrada):
    j = open(entrada,"r")
    for a in j:
        d = json.loads(a)
    j.close()
    return d


def carregabase(entrada):
    dados=open(entrada,'r')
    
    linhas = []
    
    for x in dados:
        linhas.append(x)
    
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
    dados.close
    return pronto

def keepvar(entrada,vars):
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

def media(entrada, obj):
    n,soma=0,0
    for x in entrada:
        if x[ia]==va and x[ib]==vb and x[ic]==vc and x[id]==vd:
            soma+=x[obj]
            n+=1
    try:
        med=[round(soma/n,2),n]
    except ZeroDivisionError:
        med=[None,None]
    return med

def uniquevalues(entrada,var):
    tempset=set()
    for x in entrada:
        tempset.add(x[var])
    try: tempset.remove(None)
    except KeyError: pass
    sset=sorted(tempset)
    return sset

def keepif(entrada,var,varvalue):
    temp=[]
    for x in entrada:
        if x[var]==varvalue: temp.append(x)
    return temp

def fundocalc(fundo,entrada):
    for j in range(len(entrada)):
        x=fundo[j]
        if entrada[j]=="" or entrada[j]==None: continue
        while x<entrada[j]: x*=10
        fundo[j]=x

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

def posicao(a,b,c,d,e,f):
    z=a*multiplicadores[0]+b*multiplicadores[1]+c*multiplicadores[2]+d*multiplicadores[3]+e*multiplicadores[4]+f*multiplicadores[5]
    defs=[]
    j=dados['indices'][0][a]
    defs.append(j)
    j=dados['indices'][1][b]
    defs.append(j)
    j=dados['indices'][2][c]
    defs.append(j)
    j=dados['indices'][3][d]
    defs.append(j)
    j=dados['indices'][4][e]
    defs.append(j)
    j=dados['indices'][5][f]
    defs.append(j)
    return z, defs

def lerindices(entrada):
    dimensoes=[]
    a=len(entrada['indices'][0])
    dimensoes.append(a)
    a=len(entrada['indices'][1])
    dimensoes.append(a)
    a=len(entrada['indices'][2])
    dimensoes.append(a)
    a=len(entrada['indices'][3])
    dimensoes.append(a)
    a=len(entrada['indices'][4])
    dimensoes.append(a)
    a=len(entrada['indices'][5])
    dimensoes.append(a)
    multiplicadores=[]
    b5=1
    b4=dimensoes[5]*b5
    b3=dimensoes[4]*b4
    b2=dimensoes[3]*b3
    b1=dimensoes[2]*b2
    b0=dimensoes[1]*b1
    multiplicadores.append(b0)
    multiplicadores.append(b1)
    multiplicadores.append(b2)
    multiplicadores.append(b3)
    multiplicadores.append(b4)
    multiplicadores.append(b5)
    return dimensoes, multiplicadores

def specprint(a,b,c,d,e,f):
    z,defs=posicao(a,b,c,d,e,f)
    print dados['valores'][z]
'''
dados=carrega_json('d_BRuf0115.json')

dimensoes, multiplicadores=lerindices(dados)

z,defs=posicao(5,19,1,3,2,0)
print defs
z,defs=posicao(5,18,3,2,6,0)
print defs

specprint(5,19,1,3,2,0)
specprint(5,19,1,3,2,1)
specprint(4,19,1,3,2,0)
specprint(4,19,1,3,2,1)
specprint(3,19,1,3,2,0)
specprint(3,19,1,3,2,1)
specprint(2,19,1,3,2,0)
specprint(2,19,1,3,2,1)
specprint(1,19,1,3,2,0)
specprint(1,19,1,3,2,1)
specprint(0,19,1,3,2,0)
specprint(0,19,1,3,2,1)

print "mudemos!"

specprint(5,18,3,2,6,0)
specprint(5,18,3,2,6,1)
specprint(4,18,3,2,6,0)
specprint(4,18,3,2,6,1)
specprint(3,18,3,2,6,0)
specprint(3,18,3,2,6,1)
specprint(2,18,3,2,6,0)
specprint(2,18,3,2,6,1)
specprint(1,18,3,2,6,0)
specprint(1,18,3,2,6,1)
specprint(0,18,3,2,6,0)
specprint(0,18,3,2,6,1)
'''
dados=carrega_json('d_BRuf0216.json')

dimensoes, multiplicadores=lerindices(dados)

z,defs=posicao(5,21,0,3,4,0)
print defs
z,defs=posicao(5,26,3,2,4,0)
print defs

specprint(5,21,0,3,4,0)
specprint(5,21,0,3,4,1)
specprint(4,21,0,3,4,0)
specprint(4,21,0,3,4,1)
specprint(3,21,0,3,4,0)
specprint(3,21,0,3,4,1)
specprint(2,21,0,3,4,0)
specprint(2,21,0,3,4,1)
specprint(1,21,0,3,4,0)
specprint(1,21,0,3,4,1)
specprint(0,21,0,3,4,0)
specprint(0,21,0,3,4,1)

print "nova mudança!"

specprint(5,26,3,2,4,0)
specprint(5,26,3,2,4,1)
specprint(4,26,3,2,4,0)
specprint(4,26,3,2,4,1)
specprint(3,26,3,2,4,0)
specprint(3,26,3,2,4,1)
specprint(2,26,3,2,4,0)
specprint(2,26,3,2,4,1)
specprint(1,26,3,2,4,0)
specprint(1,26,3,2,4,1)
specprint(0,26,3,2,4,0)
specprint(0,26,3,2,4,1)

'''
dados=carrega_json('d_BRuf0301.json')

dimensoes, multiplicadores=lerindices(dados)

z,defs=posicao(5,21,0,3,1,0)
print defs
z,defs=posicao(5,26,3,2,0,0)
print defs

specprint(5,21,0,3,1,0)
specprint(5,21,0,3,1,1)
specprint(4,21,0,3,1,0)
specprint(4,21,0,3,1,1)
specprint(3,21,0,3,1,0)
specprint(3,21,0,3,1,1)
specprint(2,21,0,3,1,0)
specprint(2,21,0,3,1,1)
specprint(1,21,0,3,1,0)
specprint(1,21,0,3,1,1)
specprint(0,21,0,3,1,0)
specprint(0,21,0,3,1,1)

print "mais uma mudança!"

specprint(5,26,3,2,0,0)
specprint(5,26,3,2,0,1)
specprint(4,26,3,2,0,0)
specprint(4,26,3,2,0,1)
specprint(3,26,3,2,0,0)
specprint(3,26,3,2,0,1)
specprint(2,26,3,2,0,0)
specprint(2,26,3,2,0,1)
specprint(1,26,3,2,0,0)
specprint(1,26,3,2,0,1)
specprint(0,26,3,2,0,0)
specprint(0,26,3,2,0,1)
'''

'''
    deu tudo certo, sem problemas!
'''
