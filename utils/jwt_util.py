import jwt
import datetime

from config import SECRET_KEY
from exceptions.exception_handler import ExpiredException,NotValidException


# def encode_jwt(user_id):
#     payload = {
#         'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1),
#         'iat': datetime.datetime.utcnow(),
#         'sub': user_id
#     }
#     return jwt.encode(payload, SECRET_KEY, algorithm='HS256')
#
# def decode_jwt(token):
#     try:
#         # payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
#         # return payload['sub']
#         decoded_token = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
#         return decoded_token
#     except jwt.ExpiredSignatureError:
#         raise ExpiredException('Signature expired. Please log in again.')
#         # return 'Signature expired. Please log in again.'
#     except jwt.InvalidTokenError:
#         raise NotValidException('Invalid token. Please log in again.')
#         # return 'Invalid token. Please log in again.'
