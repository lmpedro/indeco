# -*- coding: utf-8 -*-

'''
Roda os indicadores que se quiser. Eles são chamados como indX, e recebem os seguintes argumentos:
(geo='uf',ecoinit=16,ecoend=16,tamanho=5)
Ecoinit é o primeiro ecossistema para o qual se quer gerar um json, ecoend o último (geram-se todos nesse intervalo). Tamanho é o tamanho da base de dados a ser usada: 0 é a base completa, 5 a menor delas.
Deve-se importar cada indicador de seu arquivo específico.
'''

from ind1 import ind1
from ind2 import ind2
from ind3 import ind3

#ind1(geo='uf',ecoinit=1,ecoend=16,tamanho=8)
#ind1(geo='uf',ecoinit=1,ecoend=16,tamanho=9)
#ind1(geo='uf',ecoinit=1,ecoend=16,tamanho=10)
#ind1(geo='uf',ecoinit=1,ecoend=16,tamanho=11)
#ind2(geo='uf',ecoinit=1,ecoend=16,tamanho=6)
#ind2(geo='uf',ecoinit=1,ecoend=16,tamanho=7)
#ind2(geo='uf',ecoinit=1,ecoend=16,tamanho=8)
#ind2(geo='uf',ecoinit=1,ecoend=16,tamanho=9)
#ind2(geo='uf',ecoinit=1,ecoend=16,tamanho=10)
#ind1(geo='uf',ecoinit=1,ecoend=1,tamanho=5)
#ind3(geo='uf',ecoinit=1,ecoend=16,tamanho=6)
#ind3(geo='uf',ecoinit=1,ecoend=16,tamanho=7)
#ind3(geo='uf',ecoinit=1,ecoend=16,tamanho=8)
#ind3(geo='uf',ecoinit=1,ecoend=16,tamanho=9)
#ind3(geo='uf',ecoinit=1,ecoend=16,tamanho=10)
ind1(geo='uf',ecoinit=1,ecoend=16,tamanho=5)
