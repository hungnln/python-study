import uuid

from sqlalchemy import false

from app import db
from exceptions.exception_handler import NotFoundException
from models.account import Account


class AuthService:
    @staticmethod
    def firebase_token_check_account(decode_token):
        if decode_token is None:
            raise NotFoundException('Firebase token not found')
        account = Account.query.filter_by(email=decode_token['email']).first()
        if account is None:
            account = Account(
                id=uuid.uuid4().__str__(),
                username=decode_token['user_id'],
                email=decode_token['email'],
                name=decode_token['name'],
                image=decode_token['picture'],
                isActive= 0)
            print(len(account.id))
            db.session.add(account)
            db.session.commit()
        return account
