#Importamos las librerias necesarias
from flask import Blueprint
from services.todo import create_todo_service, get_todos_service, get_todo_service_by_id, upadate_service, delete_todo_service

todo = Blueprint('todo', __name__)

#Creamos la ruta inicial donde se cargarán todos los todos
@todo.route('/', methods =['GET'])
def get_todos():
    return get_todos_service()

#creamos la ruta donde en funcion del ID se mostrará su información
@todo.route('/<id>', methods = ['GET'])
def get_todo(id):
    return get_todo_service_by_id(id)

#Creamos la ruta en función del método POST para crear un todo
@todo.route('/', methods = ['POST'])
def create_todo():
    return create_todo_service()

#Creamos la ruta que en fucnión del ID, actualizará los datos
@todo.route ('/<id>' , methods = ['PUT'])
def update_todo(id):
    return upadate_service(id)

#Creamos la ruta en función del método DELETE y un ID, borrará el todo
@todo.route ('/<id>' , methods = ['DELETE'])
def delete_todo(id):
    return delete_todo_service(id)