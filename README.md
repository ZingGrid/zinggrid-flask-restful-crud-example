# zinggrid-flask-restful-crud-example

Create a REST endpoint with Python Flask Restful and have a working UI component enabling CRUD functionality in minutes!

![](https://d2ddoduugvun08.cloudfront.net/items/3r3a2x2s0w2s2a0W2c2B/Screen%20Recording%202020-02-10%20at%2003.25%20PM.gif)

## System Requirements

- python (3.7.2) -> (Required) Python is required for this project
- pip (20.0.2) -> (Required) Pip is required to install python dependencies
- flask -> The outlining REST framework to run our server. `pip install flask-restful`
- pyenv -> (recommended) pyenv is recommended to manage your python versions and package dependencies.
- pyenv-virtualenv -> (recommended) pyenv-virtualenv is recommended to keep your python (pyenv) package dependencies from leaking out.

## Flask Links
1. Flask -> https://palletsprojects.com/p/flask/
2. API Quickstart -> https://flask-restful.readthedocs.io/en/latest/quickstart.html#

## User Guide

You'll find the user guide and all documentation [here](https://flask-restful.readthedocs.io/)

## Installation Steps

1. Set python version to 3.7.2
`pyenv global 3.7.2` to set the global python version

2. Install flask with your python version`pip install flask-restful`
   
3. Setup project with `python setup.py develop`

4. Run project `python api.py` and go to [localhost:5050](http://localhost:5000/)

#### Localhost Links

The root UI is at http://localhost:5000/ and that file is `templates/zinggrid.html`

The TODO List API urls are:
- GET http://localhost:5000/todos
- POST http://localhost:5000/todos
- PUT http://localhost:5000/todos/:todo_id
- PATCH http://localhost:5000/todos/:todo_id
- GET http://localhost:5000/todos/:todo_id
- DELETE http://localhost:5000/todos/:todo_id

The TODO List API urls are:
- GET http://localhost:5000/heroes
- POST http://localhost:5000/heroes
- PUT http://localhost:5000/heroes/:id
- PATCH http://localhost:5000/heroes/:id
- GET http://localhost:5000/heroes/:id
- DELETE http://localhost:5000/heroes/:id
