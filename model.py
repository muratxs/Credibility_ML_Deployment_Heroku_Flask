# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 14:43:34 2019

@author: murat
"""
#%%

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle

#%%

df = pd.read_csv("kredi.csv", sep=";")

#%%

from pandas.api.types import CategoricalDtype
df["evDurumu"].replace("evsahibi",1, inplace = True)
df["evDurumu"].replace("kiraci",0, inplace= True)
df["telefonDurumu"].replace("var",1, inplace = True)
df["telefonDurumu"].replace("yok",0, inplace= True)
df["KrediDurumu"].replace("krediver",1, inplace = True)
df["KrediDurumu"].replace("verme",0, inplace= True)

#%%

y = df["KrediDurumu"]
X = df.drop(["KrediDurumu"], axis = 1)

#%%

from sklearn.naive_bayes import GaussianNB

nb = GaussianNB()
nb_model = nb.fit(X, y)

pickle.dump(nb_model, open("nb_model.pkl", "wb"))

#%%
model = pickle.load(open("nb_model.pkl", "rb"))
#print(model.predict([[12000, 70, 0,2,1]]))

