# from flask_restplus import Namespace, fields


# class AccountDto:
#     api = Namespace('user', description='user related operations')
#     account = api.model('account', {
#         'email': fields.String(required=True, description='user email address'),
#         'username': fields.String(required=True, description='user username'),
#         'image': fields.String(required=True, description='user image'),
#         'id': fields.String(description='user Identifier')
#     })
class ResponseDto:
    @staticmethod
    # __slots__ = ('status', 'message', 'data')
    def init(status=True, message='', data=[]):
        return {'status': status, 'message': message, 'data': data}
