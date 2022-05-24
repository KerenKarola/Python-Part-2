from crud import *
import pymongo
from bson.objectid import ObjectId

#Traer información


def FunctionJoin(tabla, tablajoin, id):
    productos = FunctionSelect(tabla,{'_id':id},'one')
    oferta = FunctionSelect(tablajoin,{'producto_id':id},'one')

    oferta.update({'productos':productos})
    print(oferta)
    

FunctionJoin('productos','ofertas',ObjectId('6216aaa4a4691436471bb611'))