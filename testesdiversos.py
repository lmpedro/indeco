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

args=cmdlparser()

geo=args.geo
ecoinit=args.ecoinit
ecoend=args.ecoend
tamanho=args.base

if args.ind==1:
    ind1(geo=geo,ecoinit=ecoinit,ecoend=ecoend,tamanho=tamanho)
elif args.ind==2:
    ind2(geo=geo,ecoinit=ecoinit,ecoend=ecoend,tamanho=tamanho)
elif arg.ind==3:
    ind3(geo=geo,ecoinit=ecoinit,ecoend=ecoend,tamanho=tamanho)
