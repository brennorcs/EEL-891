#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Universidade Federal do Rio de Janeiro
Escola Politécnica
Departamento de Engenharia Eletrônica e de Computação
Introdução ao Aprendizado de Máquina - EEL891
Professor:Heraldo Luís Silveira de Almeida
Aluno: Brenno Rodrigues de Carvalho da Silva DRE:115044743
@author: brenno
"""


#importando bibliotecas que serao utilizadas futuramente
import pandas as pd
#import featuretools as ft
#import numpy as np
import matplotlib.pyplot as plt
#import seaborn as sns 


# Carregando dados
raw_train = pd.read_csv('./train.csv')
final_test = pd.read_csv('./test.csv')

#Dividindo raw_train em conjuto de treino, validação
validation = raw_train[:int(len(raw_train)*.25)].copy()
train = raw_train[int(len(raw_train)*.25):].copy()

print('raw_train:',raw_train.shape,'\n')
print('train:', train.shape,'\n')
print('validation:',validation.shape,'\n')

#observando dados 
xs=range(3513)
ys= train['preco']
plt.bar(xs,ys)
plt.axis([0,3514,0,max(ys)])
plt.title("Histograma de Preços")
plt.xlabel("imóveis")
plt.ylabel("valor dos imoveis")
plt.show()