from flask import Blueprint, jsonify

from app.extensions import db
from app.serv.micro.roletagem import roletagem
from app.serv.micro.etnias import etnia
from app.serv.models import Ficha

fichas_api = Blueprint("fichas_api", __name__, url_prefix="/fichas")


@fichas_api.get("/criar")
def criar_ficha():
    raca = roletagem("racas", 65)
    nova_ficha = Ficha(raca, etnia(raca), roletagem("ser", 100), roletagem("classe_social", 78))
    nova_ficha.add()
    
    return jsonify(nova_ficha.to_dict()), 200

@fichas_api.get("/")
def listar_fichas():
    fichas = db.session.execute(db.Select(Ficha)).scalars()
    response = []
    for ficha in fichas:
        response.append(ficha.to_dict())
    return jsonify(response), 200