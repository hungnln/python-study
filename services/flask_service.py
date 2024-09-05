from flask import Flask
from config.db_config import DBConfig
from config.swagger_config import swagger_ui_blueprint, SWAGGER_URL

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =  DBConfig.SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = DBConfig.SQLALCHEMY_TRACK_MODIFICATIONS
app.register_blueprint(swagger_ui_blueprint, url_prefix=SWAGGER_URL)


#
# if __name__ == "__main__":
#     print(app)

