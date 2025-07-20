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
from models import db, User, Planeta, Personaje, Planetas_favoritos, Personajes_favoritos
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
def get_user_id(user_id):
    usuario = db.session.get(User,user_id)

    return jsonify(usuario.serialize()), 200



@app.route('/planeta', methods=['GET'])
def get_planeta():

    all_planeta = Planeta.query.all()
    results = list(map(lambda planeta : planeta.serialize (),all_planeta))

    response_body = {
        "planeta": results
    }

    return jsonify(response_body), 200

@app.route('/planeta/<int:planeta_id>', methods=['GET'])
def get_planeta_id(planeta_id):
    planeta = db.session.get(Planeta,planeta_id)

    return jsonify(planeta.serialize()), 200

@app.route('/personaje', methods=['GET'])
def get_personaje():
    all_personaje = Personaje.query.all()
    results = list(map(lambda personaje : personaje.serialize(),all_personaje))

    response_body = {
        "personaje": results
    }

    return jsonify(response_body), 200

@app.route('/personaje/<int:personaje_id>', methods=['GET'])
def get_personaje_id(personaje_id):
    personaje = db.session.get(Personaje,personaje_id)

    return jsonify(personaje.serialize()), 200


@app.route('/planetas_favoritos', methods=['GET'])
def get_planetas_favoritos():

    all_planetas_favoritos = Planetas_favoritos.query.all()
    results = list(map(lambda planeta : planeta.serialize (),all_planetas_favoritos))

    response_body = {
        "planetas_favoritos": results
    }

    return jsonify(response_body), 200

@app.route('/planetas_favoritos/<int:planetas_favoritos_id>', methods=['GET'])
def get_planeta_favorito(planetas_favoritos_id):
    planeta = db.session.get(Planetas_favoritos,planetas_favoritos_id)

    return jsonify(planeta.serialize()), 200

@app.route('/planetas_favoritos', methods=['POST'])
def add_planetas_favoritos():
    body = request.get_json()
    nuevo_favorito = Planetas_favoritos(**body)
    db.session.add(nuevo_favorito)
    db.session.commit()

    response_body = {
        "planetas_favoritos": nuevo_favorito.serialize (),
        "msg": "nuevo favorito"
    }

    return jsonify(response_body), 200

@app.route('/planetas_favoritos/<int:planetas_favoritos_id>', methods=['DELETE'])
def delete_planeta_favorito(planetas_favoritos_id):
    planeta_delete = db.session.get(Planetas_favoritos,planetas_favoritos_id)
    response_body ={
        "msg":"se elimino favorito"
    }

    db.session.delete(planeta_delete)
    db.session.commit()

    return jsonify(response_body), 200


@app.route('/personajes_favoritos', methods=['GET'])
def get_personajes_favoritos():

    all_personajes_favoritos = Personajes_favoritos.query.all()
    results = list(map(lambda personaje : personaje.serialize (),all_personajes_favoritos))

    response_body = {
        "personajes_favoritos": results
    }

    return jsonify(response_body), 200

@app.route('/personajes_favoritos/<int:personajes_favoritos_id>', methods=['GET'])
def get_personaje_favorito(personajes_favoritos_id):
    personaje = db.session.get(Personajes_favoritos,personajes_favoritos_id)

    return jsonify(personaje.serialize()), 200

@app.route('/personajes_favoritos', methods=['POST'])
def add_personajes_favoritos():
    body = request.get_json()
    nuevo_favorito = Personajes_favoritos(**body)
    db.session.add(nuevo_favorito)
    db.session.commit()

    response_body = {
        "planetas_favoritos": nuevo_favorito.serialize (),
        "msg": "nuevo favorito"
    }

    return jsonify(response_body), 200

@app.route('/personajes_favoritos/<int:personajes_favoritos_id>', methods=['DELETE'])
def delete_personaje_favorito(personajes_favoritos_id):
    personaje_delete = db.session.get(Personajes_favoritos,personajes_favoritos_id)
    response_body ={
        "msg":"se elimino favorito"
    }

    db.session.delete(personaje_delete)
    db.session.commit()

    return jsonify(response_body), 200



# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)

