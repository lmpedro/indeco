# -*- coding: utf-8 -*-

'''
Roda os indicadores que se quiser. Eles são chamados como indX, e recebem os seguintes argumentos:
(geo='uf',ecoinit=16,ecoend=16,tamanho=5)
Ecoinit é o primeiro ecossistema para o qual se quer gerar um json, ecoend o último (geram-se todos nesse intervalo). Tamanho é o tamanho da base de dados a ser usada:
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
Deve-se importar cada indicador de seu arquivo específico.
'''

from ind1 import ind1
from ind2 import ind2
from ind3 import ind3
from funcoes_base_inds import cmdlparser


args=cmdlparser()

geo=args.geo
ecoinit=args.ecoinit
ecoend=args.ecoend
tamanho=args.base

if args.ind==1:
    ind1(geo=geo,ecoinit=ecoinit,ecoend=ecoend,tamanho=tamanho)
elif args.ind==2:
    ind2(geo=geo,ecoinit=ecoinit,ecoend=ecoend,tamanho=tamanho)
elif args.ind==3:
    ind3(geo=geo,ecoinit=ecoinit,ecoend=ecoend,tamanho=tamanho)
