from flask import Flask
from flask_session import Session
from flask_cors import CORS
from flask_restful import Api
import simplejson as json


import os
from os.path import join, dirname


# Variaveis de sistema
from dotenv import load_dotenv
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)


# loggs
from logging.config import dictConfig

dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})




# Key
import string
import random
key_srt = string.ascii_letters + string.digits + string.ascii_uppercase
key_random = ''.join(random.choice(key_srt) for _ in range(12))


# Configs
app = Flask(__name__)
app.config['BUNDLE_ERRORS'] = True
app.config['UPLOAD_FOLDER'] = "./static/uploads"
app.config['JSON_SORT_KEYS'] = False
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.config["SESSION_COOKIE_SECURE"] = True
app.config["SESSION_COOKIE_SAMESITE"] = "lax"

# Sessão
session = Session(app)

# Configuração de APIS
api = Api(app)
CORS(app)
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'csv', 'xlsx'}
secret_key = app.config['SECRET_KEY'] = key_random
api_key = key_random

# Banco dados
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
app.config['SLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("SQLALCHEMY_DATABASE_URI")
db = SQLAlchemy(app,  engine_options={ 'connect_args': { 'connect_timeout': 1400},"pool_recycle": 120})
engine_container = db.get_engine(app)

# Serialização
ma = Marshmallow(app)


# Importando as rotas api
## from app.controllers.apis import 

# Importando as rotas de WebView
from app.controllers.view import default
