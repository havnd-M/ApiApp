from flask_sqlalchemy import SQLAlchemy
from flask import Flask, current_app , request


app = Flask(__name__)


with app.app_context():
    # within this block, current_app points to app.

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'

    db = SQLAlchemy(app)

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
    drinkInfo = Drinks.query.all()

    output = []

    for Data in drinkInfo:
        drink_data = {'name': Data.name, 'description': Data.description}
        output.append(drink_data)

    return {"drink": output}
    
@app.route('/drinks/<id>')
def get_drink(id):
    drink = Drinks.query.get_or_404(id)
    return {"name": drink.name, "description": drink.description}


@app.route('/drinks/', method=['post'])
def add_drink():
    drinks = Drinks(name=request.json['name'],
                    description=request.json['description'])
    db.session.add(drinks)
    db.session.commit()
    return {'id': drinks.id}
