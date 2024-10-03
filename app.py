import os

from dotenv import load_dotenv
from flask import Flask, jsonify, redirect
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from flask_restful import Api, MethodNotAllowed, NotFound
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

# from config.db_config import DBConfig
from utils.common import domain, port, prefix, build_swagger_config_json
from config.swagger_config import SwaggerConfig
from flask_swagger_ui import get_swaggerui_blueprint
load_dotenv()
from utils.dto import ResponseDto

# ============================================
# Main
# ============================================
app = Flask(__name__)

app.config['PROPAGATE_EXCEPTIONS'] = True
app.config.from_pyfile('./config/__init__.py')
app.config['FLASK_RUN_HOST'] = os.getenv('FLASK_RUN_HOST', '0.0.0.0')
CORS(app)
api1 = Api(app, prefix=prefix, catch_all_404s=True)
db = SQLAlchemy(app)
jwt = JWTManager(app)

# ============================================
# Swagger
# ============================================
build_swagger_config_json()
swaggerui_blueprint = get_swaggerui_blueprint(
    prefix,
    f'http://{domain}:{port}{prefix}/swagger-config',
    config={
        'app_name': "Flask API",
        "layout": "BaseLayout",
        "docExpansion": "none"
    },
)
app.register_blueprint(swaggerui_blueprint)
api1.add_resource(SwaggerConfig, '/swagger-config')
migrate = Migrate(app, db)

# api.login_firebase()



# Exception
from exceptions.exception_handler import *


@app.errorhandler(NotFoundException)
def handle_not_found(error):
   return handle_exception(error)

@app.errorhandler(AuthException)
def handle_auth_exception(error):
    return handle_exception(error)

@app.errorhandler(AccessException)
def handle_access_exception(error):
    return handle_exception(error)

@app.errorhandler(EmptyException)
def handle_empty_exception(error):
    return handle_exception(error)

@app.errorhandler(NotValidException)
def handle_not_valid_exception(error):
    return handle_exception(error)

@app.errorhandler(ExpiredException)
def handle_expired_exception(error):
    return handle_exception(error)

def handle_exception(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


