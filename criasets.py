# -*- coding: utf-8 -*-

from funcoes_base_inds import *
from conversoes import convertevar

def main():

    listabases=basesdef(12)

    vars=[]
    for i in range(34):
        vars.append(i)

    base,reduzidodef=arrumabases(listabases,vars)
    baseprofss=keepif(base[-1],26,1)

    basicas=[17,
             20,
             21,
             22,
             23,
             24,
             25,
             26,
             28,
             29,
             30,
             31,
             32,
             33,
            ]

    sets={}
    for x in basicas:
        sets[x]=uniquevalues(base[-1],x)

    sets[18]=uniquevalues(baseprofss,18)

    for eco in range(1,17):
        basee=keepif(base[-1],eco,1)
        sets[eco]=uniquevalues(basee,0)

    caminho='/Users/pedro/CTI/Python/Dashboard/Projeto Indicadores/sets.json'

    arquivo = open(caminho,"w")
    arquivo.write(json.dumps(sets))
    arquivo.close()




if __name__ == "__main__":
    main()


'''
v0   classe_cnae_20
v1   ecossis_01
v2   ecossis_02
v3   ecossis_03
v4   ecossis_04
v5   ecossis_05
v6   ecossis_06
v7   ecossis_07
v8   ecossis_08
v9   ecossis_09
v10   ecossis_10
v11   ecossis_11
v12   ecossis_12
v13   ecossis_13
v14   ecossis_14
v15   ecossis_15
v16   ecossis_16
v17   escol_fx
v18   familia
v19   idade
v20   mesorregi
v21   microrregi
v22   municipio
v23   pnivelesp
v24   pnivelger
v25   pniveltec
v26   profss
v27   sal_dez
v28   sexo
v29   sw1
v30   sw2
v31   sw3
v32   tamestab
v33   uf
'''