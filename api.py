from flask import Flask, render_template, request, jsonify
from flask_restful import reqparse, abort, Api, Resource


app = Flask(__name__)
api = Api(app)

TODOS = {
    'todo1': { 'task': 'build an API'},
    'todo2': { 'task': '?????'},
    'todo3': { 'task': 'profit!'},
}

HEROES = [
  {'id': 1, 'name': 'Batman', 'age': 55},
  {'id': 2, 'name': 'Wonder Woman', 'age': 25},
  {'id': 3, 'name': 'Damntrecky', 'age': 30},
]

class Hero:
  def __init__(self, id, name, age):
    self.id = id
    self.name = name
    self.age = age

@app.route('/')
def render_static():
    page_name = 'zinggrid'
    return render_template('%s.html' % page_name)

def abort_if_todo_doesnt_exist(todo_id):
    if todo_id not in TODOS:
        abort(404, message="Todo {} doesn't exist".format(todo_id))

# grab the array index for the HEROES
# and if it doesn't exist return a proper
# error messages
def abort_if_hero_doesnt_exist(id):
    for i, dic in enumerate(HEROES):
        if dic['id'] == int(id):
            return i
    abort(404, message="Hero {} doesn't exist".format(id))
    

parser = reqparse.RequestParser()
parser.add_argument('task')


# Todo
# shows a single todo item and lets you delete a todo item
class Todo(Resource):
    # get entry
    def get(self, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        return TODOS[todo_id]
    # delete entry
    def delete(self, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        del TODOS[todo_id]
        return '', 204
    # update cell
    def patch(self, todo_id):
        args = parser.parse_args()
        TODOS[todo_id]['task'] = args['task']
        return task, 201
    # update row
    def put(self, todo_id):
        args = parser.parse_args()
        task = {'task': args['task']}
        TODOS[todo_id] = task
        return task, 201


# TodoList
# shows a list of all todos, and lets you POST to add new tasks
class TodoList(Resource):
    # get all entries
    def get(self):
        return TODOS
    # create entry
    def post(self):
        args = parser
        todo_id = int(max(TODOS.keys()).lstrip('todo')) + 1
        todo_id = 'todo%i' % todo_id
        TODOS[todo_id] = {'task': args['task']}
        return TODOS[todo_id], 201

# Todo
# shows a single todo item and lets you delete a todo item
class Hero(Resource):
    # get entry
    def get(self, id):
        hero_index = abort_if_hero_doesnt_exist(id)
        return HEROES[int(hero_index)]
    # delete entry
    def delete(self, id):
        hero_index = abort_if_hero_doesnt_exist(id)
        del HEROES[hero_index]
        return '', 204
    # update cell
    def patch(self, id):
        hero_index = abort_if_hero_doesnt_exist(id)
        data = request.json
        hero_obj = HEROES[hero_index]
        for key in data:
            if key is not 'id':
                hero_obj[key] = data[key]
        return hero_obj, 201
    # update row
    def put(self, id):
        hero_index = abort_if_hero_doesnt_exist(id)
        data = request.json
        hero_obj = HEROES[hero_index]
        for key in data:
            if key is not 'id':
                hero_obj[key] = data[key]
        return hero_obj, 201

# HeroesList
# shows a list of all heroes, and lets you POST to add new tasks
class HeroesList(Resource):
    # get all entries
    def get(self):
        return HEROES
    # create entry
    def post(self):
        data = request.json
        data['id'] = len(HEROES) + 1
        HEROES.append(data)
        return data, 201

##
## Actually setup the Api resource routing here
##
api.add_resource(TodoList, '/todos')
api.add_resource(Todo, '/todos/<todo_id>')

api.add_resource(HeroesList, '/heroes')
api.add_resource(Hero, '/heroes/<id>')


if __name__ == '__main__':
    app.run(debug=True)