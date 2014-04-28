# -*- coding: utf-8 -*-

'''
    Arquivo para rotinas de testes. Pode ser apagado à vontade.
'''


import time
import json
from conversoes import convertecbo, converteuf, convertecnae, converteescol, convertemicro, convertemeso
import numpy as np
from funcoes_base_inds import *
import os
from functest import calculo, jsoncreate, basesdef
#ind2(geo='uf',ecoinit=1,ecoend=16,tamanho=7)
from ind1 import ind1
from ind2 import ind2
from ind3 import ind3


joe=[
     [0,1,3],
     [1,2,3],
     [10,2,4],
     [5,1,4],
      ]
arrayed=np.array(joe)
print arrayed.shape
new=arrayed.flatten()
print new
print arrayed[:,0]

black=np.average(arrayed,0)
print black

try:
    block=np.average(arrayed[:,0],weights=np.all([arrayed[:,1]==1,arrayed[:,2]==4],0),returned=1)
    print block
except ZeroDivisionError:
    block=(None, None)
    print block