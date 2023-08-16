#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 00:10:37 2023

@author: mathieudepaigne
"""

import numpy as np 

f = str(3.46)
################ f = '3.46'
L=[]
for element in f :
    L.append(element)

L[0]

import pandas as pd


btc_data = pd.read_csv('BTC.csv', index_col="Date", parse_dates= True)

print(btc_data)

btc_data.head()



btc_data1= btc_data.groupby('Volume')['Close'].sum() ###Je fais la somme des prix de fermeture qui ont le même volume de transaction
print(btc_data1)


import pandas as pd


oil_data = pd.read_csv("oil.csv")


colonne_selected = oil_data.iloc[:,[1,2]] ##Je recupère que la colonne 1 et 2 utilisation de iloc car pas de condition si ce n'est les index

#DIFFERENCE ENTRE MERGE ET CONCAT

#concat est utilisé pour empiler des DataFrames en ajoutant des lignes ou des colonnes, sans tenir compte des valeurs dans les colonnes.
#merge est utilisé pour combiner des DataFrames en utilisant des colonnes communes pour associer les lignes correspondantes.
#concat est généralement utilisé lorsque vous voulez simplement agréger des données verticalement ou horizontalement.
#merge est utilisé lorsque vous souhaitez combiner les données en fonction de colonnes correspondantes, comme lors de la fusion de tables dans une base de données.

import pandas as pd

# Supposons que vous ayez déjà les DataFrames df1 et df2

# Concaténer les DataFrames

concatenate = pd.merge(oil_data, oil_data) #Take care about the values and group in function of the commun column in the DF.

c1 = pd.concat([oil_data, oil_data], axis=1) ##axis 1 colle les colonnes et axis 0 colle les lignes


oil_data["Volume"].value_counts() #Compte le nombre de valeur pour chaque valeur de volume

print(oil_data[oil_data["Open"]<70]) #definition d'un masque idem à numpy


### bug sur comment afficher les lignes où colonne 1 est de valeur 68.22 ==> utilisation de loc

print(oil_data.loc[oil_data['Open'] == 68.22])  

print(oil_data.loc[0:2, 'Open'])


## DATA CLEANING 

oil_data= oil_data.rename(columns={'Close/Last' : 'Close'})
oil_data['volatility'] = oil_data['Close'].ewm(alpha=0.6).std() 


oil_data.replace('NaN', None, inplace=True)
oil_data = oil_data.dropna(axis=0, how='any')
mean_volatility = oil_data['volatility'].mean()
oil_data['volatility'].fillna(mean_volatility, inplace=True)
oil_data = oil_data[oil_data['Close'] >= 0] #on supprime prix négatif
# Check data
print('Valeurs NaN : \n', oil_data.isnull().sum())




L =[2,6,3,7,8]

for i in range(len(L)) :
    
    L[i]

for i in L :
