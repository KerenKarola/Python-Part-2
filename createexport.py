import collections
import pandas as pd
from pymongo import MongoClient

con = MongoClient('localhost', 27017)
db = con['sta_clara']
collection = db['productos']

# Obtener un DataFrame de la búsqueda de la colección:
datos = list(collection.find())
df = pd.DataFrame(datos)
#print(df.head())
# Exportar a Excel o CSV
# df.to_csv('productos.csv', index = False)
#df.to_excel('productos.xlsx', index=False)

# Crear una función para automatizar el export
# Debe de exportar todas las colecciones según requiera el usuario

def FunctionExport(nombre, extension, database, coleccion, indice):

    collection = db[coleccion]
    db = con[database]
    datos = list(collection.find())
    df = pd.DataFrame(datos)

    datos = list(collection.find())
    df = pd.DataFrame(datos)
    if (extension == '.csv'):
        df.to_csv(nombre + extension, index= indice)
    elif ( extension == '.xslx'):
        df.to_excel(nombre + extension, index= indice)
    print(df.head())

#FunctionExport('productos', '.csv', 'sta_clara', 'productos', False)

# def exportar_datos(formato):
#Obtener todos los nombres de las colecciones 
#     lista_collect= db.list_collection_names()
#       for name in lista_collect:
#           collection= db[name]
#     datos = list(collection.find())
#     df = pd.DataFrame(datos)

#     if formato == '.csv':
#         df.to_csv(name + '.csv', index=False)
#     elif formato == '.xlsx':
#         df.to_excel(name + '.xlsx', index=False)

# exportar_datos('productos','csv')

# dfx= pd.read_csv("productos.csv")
# print(dfx.head())

#Crear bakcup
#mongodump --db sta_clara --out C:\Users\Karola\Documents
#mongorestore db sta_clara2 C:\Users\Karola\Documents