# -*- coding: utf-8 -*-

import time
import json

def carrega_json(entrada):
    j = open(entrada,"r")
    for a in j:
        d = json.loads(a)
    j.close()
    return d

def posicao(dados,a,b,c,d,e,f):
    dimensoes, multiplicadores=lerindices(dados)
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

def specprint(dados,a,b,c,d,e,f):
    z,defs=posicao(dados,a,b,c,d,e,f)
    print dados['valores'][z]

'''
    
    
    
    
    
    
'''

#caminho='/Users/pedro/CTI/Python/Dashboard/Indicadores/Base0/'
#nomearquivo=['d_BRuf0315.json','d_BRuf0316.json']
caminho='/Users/pedro/CTI/Python/Dashboard/Indicadores/Base15/'
nomearquivo=['d_BRuf0516.json']
dados=carrega_json(caminho+nomearquivo[0])

dimensoes, multiplicadores=lerindices(dados)

z,defs=posicao(dados,5,19,1,3,0,0)
print defs
z,defs=posicao(dados,5,18,3,2,1,0)
print defs

specprint(dados,5,19,1,3,0,0)
specprint(dados,5,19,1,3,0,1)
specprint(dados,4,19,1,3,0,0)
specprint(dados,4,19,1,3,0,1)
specprint(dados,3,19,1,3,0,0)
specprint(dados,3,19,1,3,0,1)
specprint(dados,2,19,1,3,0,0)
specprint(dados,2,19,1,3,0,1)
specprint(dados,1,19,1,3,0,0)
specprint(dados,1,19,1,3,0,1)
specprint(dados,0,19,1,3,0,0)
specprint(dados,0,19,1,3,0,1)

print "mudemos!"

specprint(dados,5,18,3,2,1,0)
specprint(dados,5,18,3,2,1,1)
specprint(dados,4,18,3,2,1,0)
specprint(dados,4,18,3,2,1,1)
specprint(dados,3,18,3,2,1,0)
specprint(dados,3,18,3,2,1,1)
specprint(dados,2,18,3,2,1,0)
specprint(dados,2,18,3,2,1,1)
specprint(dados,1,18,3,2,1,0)
specprint(dados,1,18,3,2,1,1)
specprint(dados,0,18,3,2,1,0)
specprint(dados,0,18,3,2,1,1)
'''
dados=carrega_json(caminho+nomearquivo[1])

dimensoes, multiplicadores=lerindices(dados)

z,defs=posicao(dados,5,21,0,3,1,0)
print defs
z,defs=posicao(dados,5,26,3,2,1,0)
print defs

specprint(dados,5,21,0,3,1,0)
specprint(dados,5,21,0,3,1,1)
specprint(dados,4,21,0,3,1,0)
specprint(dados,4,21,0,3,1,1)
specprint(dados,3,21,0,3,1,0)
specprint(dados,3,21,0,3,1,1)
specprint(dados,2,21,0,3,1,0)
specprint(dados,2,21,0,3,1,1)
specprint(dados,1,21,0,3,1,0)
specprint(dados,1,21,0,3,1,1)
specprint(dados,0,21,0,3,1,0)
specprint(dados,0,21,0,3,1,1)

print "nova mudança!"

specprint(dados,5,26,3,2,1,0)
specprint(dados,5,26,3,2,1,1)
specprint(dados,4,26,3,2,1,0)
specprint(dados,4,26,3,2,1,1)
specprint(dados,3,26,3,2,1,0)
specprint(dados,3,26,3,2,1,1)
specprint(dados,2,26,3,2,1,0)
specprint(dados,2,26,3,2,1,1)
specprint(dados,1,26,3,2,1,0)
specprint(dados,1,26,3,2,1,1)
specprint(dados,0,26,3,2,1,0)
specprint(dados,0,26,3,2,1,1)
'''
'''
dados=carrega_json('d_BRuf0301.json')

dimensoes, multiplicadores=lerindices(dados)

z,defs=posicao(dados,5,21,0,3,1,0)
print defs
z,defs=posicao(dados,5,26,3,2,0,0)
print defs

specprint(dados,5,21,0,3,1,0)
specprint(dados,5,21,0,3,1,1)
specprint(dados,4,21,0,3,1,0)
specprint(dados,4,21,0,3,1,1)
specprint(dados,3,21,0,3,1,0)
specprint(dados,3,21,0,3,1,1)
specprint(dados,2,21,0,3,1,0)
specprint(dados,2,21,0,3,1,1)
specprint(dados,1,21,0,3,1,0)
specprint(dados,1,21,0,3,1,1)
specprint(dados,0,21,0,3,1,0)
specprint(dados,0,21,0,3,1,1)

print "mais uma mudança!"

specprint(dados,5,26,3,2,0,0)
specprint(dados,5,26,3,2,0,1)
specprint(dados,4,26,3,2,0,0)
specprint(dados,4,26,3,2,0,1)
specprint(dados,3,26,3,2,0,0)
specprint(dados,3,26,3,2,0,1)
specprint(dados,2,26,3,2,0,0)
specprint(dados,2,26,3,2,0,1)
specprint(dados,1,26,3,2,0,0)
specprint(dados,1,26,3,2,0,1)
specprint(dados,0,26,3,2,0,0)
specprint(dados,0,26,3,2,0,1)

'''

'''
    deu tudo certo, sem problemas!
'''
