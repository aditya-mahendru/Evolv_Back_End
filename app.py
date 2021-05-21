from flask import Flask, request
#from model_class import Blog
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)


class Blog(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(50), nullable=False)
    data = db.Column(db.String(1000))

    def __repr__(self):
        return f"{self.user} - {self.data}"


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

    return "Item added"


@app.route('/del_blog/<id>', methods=['DELETE'])
def delete_blog(id):
    blog = Blog.query.get(id)
    if blog is None:
        return {"!ERROR!"}
    db.session.delete(blog)
    db.session.commit()
    return "Deleted"
