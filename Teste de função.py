

def jsoncreate(results,indices,geo,neco,caminho):
    geoindex, geoname=geodef(geo)
    jresults={
        "fonte":"RAIS/MTE (2006-2011)",
        "indicador":[u"Proporção de PROFSSs","PROFSSs/trabalhadores(as)"],
        "estrutura":[
                     "Ano",
                     geoname,
                     "Classificação Nacional de Atividades Econômicas (Classe CNAE)",
                     "Faixa de Escolaridade",
                     "Sexo",
                     "Valores"],
        "indices":[
                   [2006,2007,2008,2009,2010,2011],
                   indices[0],
                   indices[1],
                   indices[2],
                   indices[3],
                   ["Proporção de PROFSSs","Número de trabalhadores(as)"],
                   ],
        "valores":list(results),
    }
    #esse if/else garante que o nome dos arquivos terá, na parte que identifica os ecossistemas, dois dígitos
    if neco<10:
        nomearquivo="d_BR"+geo+"030"+str(neco)+".json"
    else: nomearquivo="d_BR"+geo+"03"+str(neco)+".json"
    
    arquivo = open(caminho+nomearquivo,"w")
    arquivo.write(json.dumps(jresults))
    arquivo.close()


fonte [0]
indicador [1]
estrutura [5]
indices [5] com mais coisa
nind #

def jsoncreate(results,indices,geo,neco,caminho,fonte,indicador,estrutura,nind):
    geoindex, geoname=geodef(geo)
    jresults={
        "fonte":fonte,
        "indicador":indicador,
        "estrutura":estrutura,
        "indices":indices,
        "valores":list(results),
    }
    #esse if/else garante que o nome dos arquivos terá, na parte que identifica os ecossistemas, dois dígitos
    if neco<10:
        nomearquivo="d_BR"+geo+"0"+nind+"0"+str(neco)+".json"
    else: nomearquivo="d_BR"+geo+"0"+nind+str(neco)+".json"
    
    arquivo = open(caminho+nomearquivo,"w")
    arquivo.write(json.dumps(jresults))
    arquivo.close()
