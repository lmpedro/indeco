# -*- coding: utf-8 -*-

'''
    Arquivo para rotinas de testes. Pode ser apagado à vontade.
'''


import time
import json
#from conversoes import convertecbo, converteuf, convertecnae, converteescol, convertemicro, convertemeso
import numpy as np
#from funcoes_base_inds import *
import os
#from functest import calculo, jsoncreate, basesdef
#ind2(geo='uf',ecoinit=1,ecoend=16,tamanho=7)
#from ind1 import ind1
#from ind2 import ind2
#from ind3 import ind3

def uniquevalues(entrada,maskerade):
    tempset=set()
    for x in range(len(entrada)):
        if maskerade[x]:
            tempset.add(entrada[x])
    try: tempset.remove(None)
    except KeyError: pass

    sset=sorted(tempset)
    return sset


joe=[
     [0,1,3],
     [1,2,3],
     [10,2,4],
     [5,1,4],
      ]
jack=[
      [9,1,3],
      [1,9,3],
      [10,9,4],
      [5,1,9],
      ]

arrayed=np.ma.array(joe)
print arrayed.shape

vars=[0,2]
j, condition, vardef = 0, [], {}
condition=[]
for i in range(vars[-1]+1):
    if i==vars[j]:
        condition.append(1)
        vardef[vars[j]] = j
        j+=1
    else:
        condition.append(0)
print condition
print len(condition)
print vardef

jim=np.ma.compress(condition, joe, axis=1)

joe=np.ma.array(joe)
jack=np.ma.array(jack)

print jim
print joe, jack


john = np.ma.array([joe,jack])
print john
print joe.shape, jack.shape, john.shape

print "here"
try:
    print jack.shape
    jack=np.ma.array([jack,joe])
except NameError:
    jack=np.ma.array(joe)

print jack
print jack.shape

print "johny is", john[-1,:,1]
maskerade=np.any(np.array([john[-1,:,1]==9,john[-1,:,1]==8]),0)
print maskerade
#john=np.ma.array(john,mask=[maskerade,maskerade,maskerade,maskerade,maskerade,maskerade])
ad=uniquevalues(john[-1,:,1],maskerade)
print ad
print "äsdasdasD"
print john
print john[0,:,1]

def setdef(base,controlador,neconum=0,onlyprofss=0):
    sets=[]
    sets.append(uniquevalues(base[:,controlador[3]],np.ones(len(base[:,controlador[3]]))))
    maskerade=np.array(base[:,controlador[1]]==neconum)
    sets.append(uniquevalues(base[:,controlador[4]],maskerade))
    h=5
    for x in onlyprofss:
        if x:
            maskeradeb=np.all((np.array(base[:,controlador[2]]==1),maskerade),0)
            sets.append(uniquevalues(base[:,controlador[h]],maskeradeb))
            print maskeradeb
        else:
            sets.append(uniquevalues(base[:,controlador[h]],maskerade))
            print maskerade
        h+=1
    print sets
    return sets

setdef(joe,[0,1,0,2,1,0,0],2,[0,1])

try:
    john[0,1,0]
    print len(john)
except all:
    pass

bloke=np.empty(0)
print bloke

bloke=np.append(bloke,np.array(3))
bloke=np.append(bloke,np.array(2))
#bloke=np.hstack((bloke,np.array(1)))
#bloke=np.hstack((bloke,np.array(1)))
print bloke
print bloke.shape
bi=np.array([bloke,bloke])
print bi
bi

print john[1,:,0]
print np.ma.average(john[1,:,0]==1)

#controls: lista com sete ints que indicam a posição da variável objetiva [0], da variável de ecossistemas[1], da variável de profss[2], da variável geográfica[3], da variável de cnaes[4] e das duas variáveis de controle específicas [5-6] na base de dados


'''
def rodar(bases,defs,geo,neco):
    neconum=ecotransform(neco)
    reduzido=bases[-1]
    geoindex, geoname=geodef(geo)
    
    #controls: lista com cinco ints que indicam a posição da variável objetiva [0] e das variáveis de controle [1-4] na base de dados
    controls=[
              defs[29],
              int(defs[geoindex]),
              defs[0],
              defs[17],
              defs[19],
              ]
              
    #sets: lista com quatro elementos, cada um deles um set dos valores únicos pelos quais se deve iterar as variáveis de controle

    #criar os conjuntos de valores através dos quais se deve iterar ao calcular as médias. Geram-se listas ordenadas dos valores únicos de uf, cnae... Resume-se a base às observações do ecossistema para restringir o conjunto de cnaes àquelas do ecossistema, e retiram-se observações que não sejam de profss para captar apenas as CBOs dessa categoria.
    sets=[]
    sets.append(uniquevalues(reduzido,controls[1]))
    #retirar observações que não são do ecossistema em questão
    reduzidobeta=keepif(reduzido,defs[neconum],1)
    sets.append(uniquevalues(reduzidobeta,controls[2]))
    sets.append(uniquevalues(reduzido,controls[3]))
    #retirar observações que não são de PROFSSs
    reduzido=keepif(reduzido,defs[28],1)
    sets.append(uniquevalues(reduzido,controls[4]))

    #identifica se a função utiliza dados de todos os trabalhadores ou somente de PROFSSs e a posição da variável de PROFSSs
    onlyprofss=[1,defs[28]]
'''