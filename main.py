
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Season(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.string(300), nullable = False)
    question_a =db.Column(db.string(50), nullable = False)
    question_b = db.Column(db.string(50), nullable = False)
    question_c = db.Column(db.string(50), nullable = False)
    question_d = db.Column(db.string(50), nullable = False)
    answer = db.Column(db.string(15), nullable = False)
