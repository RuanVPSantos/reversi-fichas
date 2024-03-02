from flask import Flask

from flask_cors import CORS

from config import Config
from app.routes.fichas import fichas_api
from app.extensions import db

objeto = Flask(__name__)
objeto.config.from_object(Config)
objeto.config["SESSION_PERMANENT"] = False
objeto.config["SESSION_TYPE"] = "filesystem"
cors = CORS(objeto)
objeto.config["CORS_HEADERS"] = "Content-Type"

db.init_app(objeto)

objeto.register_blueprint(fichas_api)

app = objeto
