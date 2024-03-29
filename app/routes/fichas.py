from flask import Blueprint, jsonify
from sqlalchemy import desc
import pandas as pd

from app.extensions import db
from app.serv.micro.roletagem import roletagem
from app.serv.micro.etnias import etnia
from app.serv.models import Ficha


fichas_api = Blueprint("fichas_api", __name__, url_prefix="/fichas")


@fichas_api.get("/criar/")
def criar_ficha():
    raca = roletagem("racas", 65)
    nova_ficha = Ficha(raca, etnia(raca), roletagem("ser", 100), roletagem("classe_social", 78))
    nova_ficha.add()
    
    return jsonify(nova_ficha.to_dict()), 200



@fichas_api.get("/criar_lote/<int:qtd>/")
def criar_lote(qtd):
    fichas = []
    for i in range(qtd):
        raca = roletagem("racas", 65)
        nova_ficha =  Ficha(raca, etnia(raca), roletagem("ser", 100), roletagem("classe_social", 78))
        print(f'fase 1, item {i}')
        fichas.append(nova_ficha)
    for i in range(len(fichas)):
        db.session.add(fichas[i])
        print(f'fase 2, item{i}')
    db.session.commit()
    return {}, 200

@fichas_api.get("/dados_seres/")
def enviar_dados():
    all_data = db.session.execute(db.select(Ficha)).scalars()
    df = pd.DataFrame([i.to_dict() for i in all_data])
    dados = df.groupby(['etnia'], group_keys=True, as_index=False).count().sort_values('raca', ascending=False)
    # print(dados)
    resp = []
    for linha in dados.iloc:
        resp.append({'etnia' : linha['etnia'], 'percentual' : round(linha['raca'] / len(df) * 100, 2)})
    return jsonify(resp), 200


@fichas_api.get("/")
def listar_fichas():
    fichas = db.session.execute(db.Select(Ficha).order_by(Ficha.id.desc())).scalars()
    response = []
    for ficha in fichas:
        response.append(ficha.to_dict())
    return jsonify(response), 200