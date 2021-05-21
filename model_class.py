from flask import Flask
from sqlalchemy_serializer import SerializerMixin
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


db = SQLAlchemy(app)


class Blog(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(50), nullable=False)
    data = db.Column(db.String(1000))

    def __repr__(self):
        return f"{self.user} - {self.data}"
