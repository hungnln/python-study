import os
from datetime import datetime, timedelta
from functools import wraps

import jwt
from dotenv import load_dotenv
from flask import make_response, request, jsonify

from exceptions.exception_handler import ExpiredException, NotValidException
# from exceptions.exception_handler import  *
# from utils.jwt_util import decode_jwt
from utils.response import Response
load_dotenv()

class JWTConfig:
    JWT_BLACKLIST_ENABLED = True
    JWT_BLACKLIST_TOKEN_CHECKS = ['access', 'refresh']
    JWT_BLACKLIST_AFTER_ROTATION = True
    SECRET_KEY=os.environ.get('SECRET_KEY')
    JWT_SECRET_KEY=os.environ.get('JWT_SECRET_KEY')
    JWT_TOKEN_LOCATION=os.environ.get('JWT_TOKEN_LOCATION')
    @staticmethod
    def createToken(user,is_admin):
        role = "admin" if is_admin else "user"
        token = jwt.encode(
            payload={
                'user_id': user.id,
                'username': user.name,
                'iat': datetime.utcnow(),
                'exp': datetime.utcnow() + timedelta(minutes=30),
                'role': "admin" if is_admin else "user"
                # 'authorities': 'USER'
            }, key=JWTConfig.SECRET_KEY, algorithm='HS256')
        return token
    @staticmethod
    def validateToken(token):
        try:
            jwt.decode(token, key=JWTConfig.SECRET_KEY, algorithms=['HS256'])
            return True
        except jwt.ExpiredSignatureError:
            return Response.make(status=False, msg='Expired token')
        except jwt.InvalidTokenError:
            return Response.make(status=False, msg='Invalid token')
    @staticmethod
    def setCookie(token):
        success_login = {'status': True, 'msg': 'Login Success'}
        response = make_response(success_login)
        response.set_cookie('x-auth-token', token)
        return response
    @staticmethod
    def logOut():
        resp = make_response({'status': True, 'msg': 'Logout Success'})
        resp.delete_cookie('x-auth-token')
        return resp
    @staticmethod
    def role_required(required_role):
        def decorator(fn):
            @wraps(fn)
            def wrapper(*args, **kwargs):
                # Get the token from the Authorization header
                auth_header = request.headers.get('Authorization', None)
                if not auth_header:
                    response = Response.make(status=False, msg='Missing token')
                    return jsonify(response), 401
                    # raise AuthException("Missing token")

                # Split "Bearer" and the token
                try:
                    token = auth_header.split()[1]
                except IndexError:
                    response = Response.make(status=False, msg='Invalid token format')
                    return jsonify(response), 401
                    # raise NotValidException('Invalid token format')

                # Decode the token
                decoded_token = JWTConfig.decode_jwt(token)
                if not decoded_token:
                    return jsonify(msg="Invalid or expired token"), 401
                    # raise NotValidException('Invalid or expire token')

                # Check if the user's role matches the required role
                if decoded_token.get("role") != required_role:
                    return jsonify(msg="Insufficient permissions"), 403
                    # raise AccessException('Insufficient permissions')

                return fn(*args, **kwargs)

            return wrapper

        return decorator
    @staticmethod
    def encode_jwt(user_id):
        payload = {
            'exp': datetime.utcnow() + timedelta(days=1),
            'iat': datetime.utcnow(),
            'sub': user_id
        }
        return jwt.encode(payload, JWTConfig.SECRET_KEY, algorithm='HS256')
    @staticmethod
    def decode_jwt(token):
        try:
            # payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
            # return payload['sub']
            decoded_token = jwt.decode(token, JWTConfig.SECRET_KEY, algorithms=["HS256"])
            return decoded_token
        except jwt.ExpiredSignatureError:
            raise ExpiredException('Signature expired. Please log in again.')
            # return 'Signature expired. Please log in again.'
        except jwt.InvalidTokenError:
            raise NotValidException('Invalid token. Please log in again.')
            # return 'Invalid token. Please log in again.'