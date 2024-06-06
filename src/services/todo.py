#Importamos las librerias necesarias
from flask import request, Response
from bson import json_util, ObjectId
#Importamos la configuración de la BBDD
from config.mongodb import mongo

#Creamos la fucnión para crear un todo
def create_todo_service():
    data = request.get_json()
    title = data.get('title', None)
    description = data.get('description', None)
    if title:
        response = mongo.db.todos.insert_one({
            'title' : title,
            'description' : description,
            'done' : False
        })
        result = {
            'id' : str(response.inserted_id),
            'title' : title,
            'description' : description,
            'done' : False
        }
        return result
    else:
        return 'Invalid payload', 400


#Creamos la función para cargar los todos creados    
def get_todos_service():
    data = mongo.db.todos.find()
    result = json_util.dumps(data)
    return Response(result, mimetype = 'application/json')


#Creamos la función de mostrar los datos de un todo en función de su ID
def get_todo_service_by_id(id):
    data = mongo.db.todos.find_one({'_id' : ObjectId(id)})
    result = json_util.dumps(data)
    return Response(result, mimetype = 'application/json')


#Creamos la fucción que se usará para modificar los datos de un todo
def upadate_service(id):
    data = request.get_json()
    if len(data) == 0:
        return 'invalid payload', 400
    
    response = mongo.db.todos.update_one({'_id' : ObjectId(id)}, {'$set' : data})
    
    if response.modified_count >= 1:
        return 'Todo update succesfully', 200
    else:
        return 'Todo not found', 404


#Definimos la función que eliminará el todo en función de su ID    
def delete_todo_service(id):
    response = mongo.db.todos.delete_one({'_id' : ObjectId(id)})
    if response.deleted_count >=1:
        return 'Todo deleted succesfully', 200
    else:
        return 'Todo not found', 404