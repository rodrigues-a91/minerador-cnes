# -*- coding: utf-8 -*-
"""
Created on Tue May 25 16:24:54 2021

@author: Carlos Alberto
"""

import pandas as pd
from unicodedata import normalize
 

def tratarNomeDosCampos(df):
    nomeDasColunas = df.columns.values
    for nomeDaColuna in nomeDasColunas:
        
        nomeDaColunaSemEspaco = nomeDaColuna.replace(" ","_").lower()
        nomeColunaPadronizada = normalize('NFKD', nomeDaColunaSemEspaco).encode('ASCII','ignore').decode('ASCII')
        df = df.rename(columns={nomeDaColuna:nomeColunaPadronizada})
    return df

def normalizarDados(listDocuments):
    df = pd.json_normalize(listDocuments)
    df = tratarNomeDosCampos(df)
    df['codmunicipio'] = df['municipio'].apply(lambda conteudo: conteudo.split(' - ')[0])
    df['municipio'] = df['municipio'].apply(lambda conteudo: conteudo.split(' - ')[1])
    df = df.replace(to_replace='---', value='')
    df = df.replace(to_replace='--', value='')

    keys = df.columns.values
    
    return df
    