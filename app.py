from flask import Flask, request
from model_class import Blog
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)


@app.route('/all_blogs')
def get_blogs():
    output = []

    blogs = Blog.query.all()
    for blog in blogs:
        output.append(blog.to_dict())

    return {"Blogs": output}


@app.route('/all_blogs/<id>')
def get_blog(id):
    return Blog.query.get_or_404(id).to_dict()

@app.route('/add_blog', methods=['POST'])
def add_blog():
    blog = Blog(user=request.json['user'], data=request.json['data'])
    db.session.add(blog)
    db.session.commit()

    return "Item added at id"
