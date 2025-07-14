"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, Planetas, Personajes
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False

db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace("postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/user', methods=['GET'])
def get_user():
    all_users = User.query.all()
    results = list(map(lambda user : user.serialize(),all_users))

    response_body = {
        "user": results
    }

    return jsonify(response_body), 200

@app.route('/user/<int:user_id>', methods=['GET'])
def get_usuario(user_id):
    usuario = db.session.get(User,user_id)

    return jsonify(usuario.serialize()), 200



@app.route('/planetas', methods=['GET'])
def get_planetas():

    all_planetas = Planetas.query.all()
    results = list(map(lambda planeta : planeta.serialize (),all_planetas))

    response_body = {
        "planetas": results
    }

    return jsonify(response_body), 200

@app.route('/planetas/<int:planetas_id>', methods=['GET'])
def get_planet(planetas_id):
    planet = db.session.get(Planetas,planetas_id)

    return jsonify(planet.serialize()), 200

@app.route('/personajes', methods=['GET'])
def get_personajes():
    all_personajes = Personajes.query.all()
    results = list(map(lambda personajes : personajes.serialize(),all_personajes))

    response_body = {
        "personajes": results
    }

    return jsonify(response_body), 200

@app.route('/personajes/<int:personajes_id>', methods=['GET'])
def get_personaje(personajes_id):
    personaje = db.session.get(Personajes,personajes_id)

    return jsonify(personaje.serialize()), 200

# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
