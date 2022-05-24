
# from crud import *
# import datetime

# def updatekardex(action,tabla):
# 	current_time=datetime.datetime.now()
# 	data_log = {
# 		'action': action,
# 		'fecha' : current_time,
# 		'tabla' : tabla
# 	}
# 	FunctionInsert('log',data_log)



# datos_producto = {
#     "nombre": 'Clonazepam',
#     "lote": '3020abc',
#     "descripción": "Reduce el insomnio",
#     "desc": 0,
#     "precio": 312,
#     "departamento": "Antidepresivos",
#     "stock":122,
# 	"receta": True
    
# }

# FunctionInsert('productos',datos_producto)
# FunctionSelect('log',{},'all')

# #Traer datos de la BD
# def FunctionSelect(tabla,buscar,tipo):
# 	collection = db[tabla]
# 	if tipo == 'one':
# 		resultados=collection.find_one(buscar)
# 	elif tipo =='all':
# 		resultados=list(collection.find(buscar))
# 	#Print a variable resultados
# 	return(resultados)


# #Insertar datos
# def FunctionInsert(tabla, datos):
# 	collection = db[tabla]
# 	if type(datos) == list:
# 		collection.insert_many(datos)
# 	else:
# 		collection.insert_one(datos)

# 	FunctionSelect(tabla)

# #Eliminar datos
# def FunctionDelete(tabla,dato):
# 	if type(dato)==list:
# 			tabla.delete_many(dato)
# 	else:
# 			tabla.delete_one(dato)

# #Update



# def FunctionUpdate(tabla, find, values):
# 	new_values= {'$set':values}

# 	if type(find)==list:
# 		tabla.update_many(find, new_values)
# 	else:
# 		tabla.update_one(find, new_values)

# datos = { "precio": "82" }
# newdatos = { "precio": "52" }




#Paso 1.- Crear un entorno virtual
#python -m venv venv venv

#Paso 2.- Instalar pymongo
#pip install pymongo

#Paso 3.- Activar el entorno virtual
#venv\scripts\activate

#Paso 4.- Ejecutar el archivo
#python nombredearchivo

#Revisar que tenemos instalado de manera global
#pip freeze

