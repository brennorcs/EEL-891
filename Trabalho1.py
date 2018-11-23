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
import matplotlib.pyplot as plt
import numpy as np



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
ys=train['preco']
xs=range(3513)
plt.scatter(xs,ys)
plt.show()

#Removendo outliers
train = train.drop(train[train.preco > 1e7].index)
ys=train['preco']
xs=range(0, len(train['preco']))
plt.scatter(xs,ys)
plt.show()
