from flask import Flask

app = Flask(__name__)
from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)


class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(50), nullable=False)
    data = db.Column(db.String(1000))

    def __repr__(self):
        return f"{self.user} - {self.data}"


@app.route('/all_blogs')
def get_blogs():
    blogs = Blog.query.all()
    return {"Blogs": blogs}
