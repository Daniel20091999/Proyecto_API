from flask import Blueprint

todo = Blueprint('todo', __name__)

@todo.route('/', methods =['GET'])
def get_todos():
    return 'get all todos'

@todo.route('/<id>', methods = ['GET'])
def get_todo():
    return 'Get todo by id'

@todo.route('/', methods = ['POST'])
def create_todo():
    return 'Create todo'

@todo.route ('/<id>' , methods = ['PUT'])
def update_todo():
    return 'Update todo'

@todo.route ('/<id>' , methods = ['DELETE'])
def delete_todo():
    return 'Delete todo'