
import pymongo
from pymongo import MongoClient

con = MongoClient('localhost', 27017)
db = con['sistemas_escolares']



def FunctionInsert(tabla, datos):
    collection = db[tabla]
    if type(datos) == list:
        collection.insert_many(datos)
    else:
        collection.insert_one(datos)

# FunctionInsert('alumnos', {
#     'nombre': 'Keren',
#     'apellido':'Corral',
#     'carrera':'DGS'
# })
# FunctionInsert('materias',
# 	{'nombre': 'matematicas'},
# 	{'nombre':'Español'}])

# FunctionInsert('calificaciones',
# [{
# 	'alumno_id':'62267848694cb778e5d56df9',
# 	'materia_id':'62267915405b8d9d34063b58',
# 	'calificacion':90
# },
# {
# 	'alumno_id':'62267848694cb778e5d56df9',
# 	'materia_id':'62267915405b8d9d34063b59',
# 	'calificacion':90	

# }])

# FunctionInsert('kardex',
# {
# 	'alumno_id':'62267848694cb778e5d56df9',
# 	'promedio':80
# })


# #Eliminar datos
# def FunctionDelete(tabla,dato):
# 	collection = db[tabla]
# 	if type(dato)==list:
# 			collection.delete_many(dato)
# 	else:
# 			collection.delete_one(dato)

#FunctionDelete('productos',{'nombre':'Omperazol'})
#FunctionSelect('productos','')

def FunctionUpdate(tabla, find, values):
    collection = db[tabla]

    new_values = {"$set": values}
    if type(find) == list:
        collection.update_many(find, new_values)
    else:
        collection.update_one(find, new_values)


FunctionUpdate('calificaciones', {'promedio':100}, {'promedio':70})



