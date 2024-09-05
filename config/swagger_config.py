from flask_swagger_ui import get_swaggerui_blueprint

# SWAGGER_URL="/swagger"
# API_URL="/static/config.json"
#
# swagger_ui_blueprint = get_swaggerui_blueprint(
#     SWAGGER_URL,
#     API_URL,
#     config={
#         'app_name': 'Access API'
#     }
# )
from flask_restful import Resource
from flask import jsonify
import json

class SwaggerConfig(Resource):
    def get(self):
        with open('static/swagger/config.json', 'r') as config_file:
            config_data = json.load(config_file)
        return jsonify(config_data)
