# Evolv Back End

APIs for CRUD operations on a Database handling blogs.

## Install

This project needs 

* Flask:
 
`pip3 install flask`

* Flask-SQLALchemy:

`pip3 install flask-sqlalchemy`

* SQLAlchemy-serializer:
 
`pip3 install SQLAlchemy-serializer`

to work correctly.

To install the project repo, run the following git command:

`https://github.com/aditya-mahendru/Evolv_Back_End.git`

## Usage

For basic execution:

`export FLASK_APP = app.py`

`export FLASK_ENT = development`
to enable debug mode.

`flask run`

## APIs

|API|Route|Comments|
|--------|---------|-------------|
|POST|`/add_blog`|-|
|GET|`/all_blogs`|-|
|GET|`/all_blogs/<id>`|Blog at `id`|
|DELETE|`/del_blog/<id>`|-|
|PUT|`/update_blog/<id>`|-|


  
