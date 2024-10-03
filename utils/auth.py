from config.jwt_config import JWTConfig
from utils.response import Response
from flask import request
from functools import wraps
import jwt

class Auth:
    def middleware(self, func):
        @wraps(func)
        def decorator():
            token=request.cookies.get('x-auth-token')
            if not token:
                return Response.make(False,'Forbidden access')
            try:
                jwt.decode(token, JWTConfig.JWT_SECRET_KEY, algorithms='HS256')
            except jwt.ExpiredSignatureError:
                return Response.make(False, 'Unauthorized')
            except jwt.InvalidTokenError:
                return Response.make(False, 'Invalid token')
            return func()
        return decorator