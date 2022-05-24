######Farmacia santa_clara#####
#Agrega la libería general de pymongo
import pymongo
#Agrega la función de mongo cliente desde pymongo
from pymongo import MongoClient

#Se crea la conexión con Mongo
con		 = MongoClient('localhost',27017)
#Seleccionar la BD
db			= con['sta_clara']
collection	= db['usuarios']  

usuarios = {
    "nombre": "Luis",
    "apellido": "Alvarado",
    "edad": 22,
    "tel": 6182221188,
    "correo": "luis.2001@gmail.com",
    "dirección":{
        "calle":'',
        "num_ext":'' ,
        "num_ext":'' ,
        "municipio":'' ,
        "estado":'' ,
        "cp":'',

    },
    "token_pago":'',
    "sexo": 'Mujer',


}

producto = {
    "nombre"
    "lote": "Luis",
    "descripción": "Alvarado",
    "desc": 22,
    "precio": 6182221188,
    "departamento": "luis.2001@gmail.com",
    "stock":'',
    "descuento":"",
    
}

checkout={
    "metodo_pago": "",
    "titular": "Luis",
    "fecha_trans": " ",
    "hora_trans": "",
    "iva": 0.16,
    "items": {
        "producto_id":"",
        "cantidad":'',
        "total":''
    },
    "token_usuario":'',
    "status":"",
    "costo_envio":""
}

carrito={
    "nombre":'',
    "producto_id":"",
    "cantidad":"",
    "subtotal":'',
    "iva":"",
    "total":""
}


ofertas={
    "producto_id":'',
    "precio":"",
    "descuento":"",
    "fecha_inicio":"",
    "fecha_fin":""
}

