from flask import jsonify

from  app import app
from controllers.auth_controller import AuthController
from utils.auth import Auth
from config.jwt_config import JWTConfig

auth = Auth()
@app.post('/login-firebase')
def login_firebase():
    return AuthController().login_firebase()



# Protected route for admin access only
def role_required(param):
    pass


@app.route('/admin', methods=['GET'])
# @JWTConfig.role_required('admin')  # Only admin can access this route
def admin_route():
    return jsonify(msg="Welcome, admin!"), 200

# Protected route for user access only
@app.route('/user', methods=['GET'])
@JWTConfig.role_required('user')  # Only users with 'user' role can access
def user_route():
    return jsonify(msg="Welcome, user!"), 200