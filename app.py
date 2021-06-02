# -*- coding: utf-8 -*-
"""
Created on Fri May 21 16:48:28 2021

@author: Carlos Alberto
"""
import functions.entradaDeDados as entradaDeDados
import functions.normalizacaoDosDados as normalizacaoDosDados
import functions.saidaDeDados as saidaDeDados

url = 'http://cnes.datasus.gov.br/pages/estabelecimentos/consulta.jsp?search=UPA'

listDocuments = entradaDeDados.minerarOsDadosDoBotao(url)

df = normalizacaoDosDados.normalizarDados(listDocuments)

saidaDeDados.gerarArquivosDeSaida(df)


