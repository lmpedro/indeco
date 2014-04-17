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

caminho='/Users/pedro/CTI/Python/Dashboard/Indicadores/Base0/d_BRuf'

for w in range(3,4):

    for q in range(1,17):
        jota=[]
        for x in range(6,12):
            
            if q<10:
                nomele='/Users/pedro/CTI/Python/Dashboard/Indicadores/Base'+str(x)+'/d_BRuf0'+str(w)+'0'+str(q)+'.json'
            else:
                nomele='/Users/pedro/CTI/Python/Dashboard/Indicadores/Base'+str(x)+'/d_BRuf0'+str(w)+str(q)+'.json'
            
            dados=carrega_json(nomele)
            for gama in dados['valores']:
                jota.append(gama)

        dados['valores']=jota

        if q<10:
            nomegrava=caminho+'0'+str(w)+'0'+str(q)+'.json'
        else:
            nomegrava=caminho+'0'+str(w)+str(q)+'.json'
        arquivo = open(nomegrava,"w")
        arquivo.write(json.dumps(dados))
        arquivo.close()
