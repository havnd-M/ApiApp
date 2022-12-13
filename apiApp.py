from flask_sqlalchemy import SQLAlchemy
from flask import Flask, current_app


app = Flask(__name__)


with app.app_context():
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
    #app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db = SQLAlchemy(app)
    # within this block, current_app points to app.

    class Drinks(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String(100), unique=True, nullable=False)
        description = db.Column(db.String(120))

        def __repr__(self):
            return f"{self.name} - {self.description}"
    print(current_app.name)


@app.route('/')
def index():
    return "hello"


@app.route('/drinks')
def drinks():
    return {"drink": "coca cola"}
