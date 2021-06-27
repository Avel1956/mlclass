from Class_functions import*
from xploreapi import XPLORE
import pandas as pd
#import xplore
def open_csv (filename):
#Esta funcion tiene como entrada el nombre de un archivo en el workpath con formato 
#.csv y devuelve un dataframe con los contenidos del archivo con los 
#contenidos de la primera fila como encabezados.
    df = pd.read_csv (filename)
    return df

df = open_csv("api_ref.csv")
key = df['key'][2]

query = XPLORE(key)
query.authorText('Natalia Gaviria Gomez')
query.dataType('json')
query.dataFormat('object')
data = query.callAPI()

# gittest
write_json(data)
print(data)



