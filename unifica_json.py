# -*- coding: utf-8 -*-

import time
import json
import numpy as np
from funcoes_base_inds import carrega_json

def juncao(geo='uf',ind=1):
    caminho='/Users/pedro/CTI/Python/Dashboard/Indicadores/Base0/d_BR%s' % geo

    for q in range(1,17):
        jota=[]
        for x in range(6,12):
            
            nomele='/Users/pedro/CTI/Python/Dashboard/Indicadores/Base%i/d_BR%s%02i%02i.json' % (x, geo, ind, q)
            
            dados=carrega_json(nomele)
            for gama in dados['valores']:
                jota.append(gama)

        dados['valores']=jota

        nomegrava='%s%02i%02i.json' % (caminho, ind, q)
        arquivo = open(nomegrava,"w")
        arquivo.write(json.dumps(dados))
        arquivo.close()

if __name__ == '__main__':
    juncao(geo='meso',ind=1)