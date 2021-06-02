# -*- coding: utf-8 -*-
"""
Created on Thu May 13 09:15:23 2021

@author: Carlos Alberto
"""


def gerarArquivosDeSaida(dataFrame):
    
   outputPath = 'data/output/'

   with open (outputPath + 'unidades-de-pronto-atendimento.csv', 'w+', encoding='utf8') as dataFrameOutput:
       dataFrame.to_csv(dataFrameOutput, sep=';', index=False, line_terminator='\n')

    

