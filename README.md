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

`export FLASK_ENV = development`
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

**Postman:**
[![Run in Postman](https://run.pstmn.io/button.svg)](https://god.gw.postman.com/run-collection/15819335-67ee9064-71dc-43d6-8829-cdec10d3cac2?action=collection%2Ffork&collection-url=entityId%3D15819335-67ee9064-71dc-43d6-8829-cdec10d3cac2%26entityType%3Dcollection%26workspaceId%3D545445f2-c9f2-4e78-9a38-da7379e3ef1b)
