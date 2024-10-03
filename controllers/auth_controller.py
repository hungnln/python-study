from datetime import datetime, timedelta
from typing import Dict

import jwt
from firebase_admin import auth

from firebase_admin.exceptions import FirebaseError
from flask import jsonify, request, make_response

from config import JWTConfig
from exceptions.exception_handler import NotValidException, ExpiredException
from services.auth_service import AuthService
from utils.dto import ResponseDto
from utils.response import Response


class AuthController:
    def login_firebase(self):
        global decode_token
        token = request.json.get('token')
        print(token)
        try:
            if token is not None or token!= "":
                decode_token = auth.verify_id_token(token)
                print(f"Decode token: \n{decode_token}")
        except auth.ExpiredIdTokenError as e:
            # return Response.make(False,"Expired Id Token")
            raise ExpiredException('Expired Id Token')
        except auth.InvalidIdTokenError as e:
            # return Response.make(False,"Invalid Id Token")
            raise NotValidException('Invalid Id Token')
        account = AuthService.firebase_token_check_account(decode_token)
        token = JWTConfig.createToken(account,False)
        print(f"check response:{account.to_dict()}")
        data = {
            "account":account.to_dict(),
            "token":token
        }
        response = Response.make(True, "Login success",data)
        return jsonify(response),200
