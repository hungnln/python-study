import os
from dotenv import load_dotenv
load_dotenv()

class JWTConfig:
    JWT_BLACKLIST_ENABLED = True
    JWT_BLACKLIST_TOKEN_CHECKS = ['access', 'refresh']
    JWT_BLACKLIST_AFTER_ROTATION = True
    SECRET_KEY=os.environ.get('SECRET_KEY')
    JWT_SECRET_KEY=os.environ.get('JWT_SECRET_KEY')
    JWT_TOKEN_LOCATION=os.environ.get('JWT_TOKEN_LOCATION')