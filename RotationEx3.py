# -- coding: utf-8 --
"""
Created on Thu Mar  2 22:13:39 2023

@author: NATGF
"""


import json
import pandas as pd


dados_arquivo = pd.read_json('C:/Users/NATGF/Downloads/dados 1 desafio.json')
print(dados_arquivo)
print(dados_arquivo.columns)
dia = dados_arquivo['dia']
valor = dados_arquivo['valor']

maior = 0
menor = 99999999
soma = 0
qtd = 0
for i in range(len(valor)):
    if (valor[i] != 0):
        if (valor[i] > maior):
            maior = valor[i]
            
        if (valor[i] < menor):
            menor = valor[i]
            
        soma = soma + valor[i]
        qtd = qtd + 1;

print('Maior valor de faturamento: ',maior)
print('Menor valor de faturamento: ',menor)

media = soma/qtd
print('Media: ',media) 

qtdDiasMaior = 0;
for i in range(len(valor)):
    if (valor[i] > media):
       qtdDiasMaior = qtdDiasMaior + 1

print(qtdDiasMaior, ' dias que houveram faturamento maior que a media.')