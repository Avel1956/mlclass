#Jaime Andrés Vélez, 2021
#Analisis, representacion y clasificación de textos


from tabulate import tabulate
from Class_functions import *
from mlmodels import *
import os
import sys




df = open_csv("references.csv")
#col_perc_nan(df, 10)

vect_text = toke_vect(df, "Abstract")
print(vect_text)

X_train, X_test, y_train, y_test = split_sample(df, vect_text)