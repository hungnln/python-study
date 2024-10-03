from flask import jsonify

# from app import app


class NotFoundException(Exception):
    status_code = 404
    status=False
    def __init__(self, message='',status_code=None,payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload
    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        rv['status'] = self.status
        return rv

class AuthException(Exception):
    status_code = 401
    status = False
    def __init__(self, message='',status_code=None,payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload
    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        rv['status'] = self.status
        return rv

class AccessException(Exception):
    status_code = 403
    status = False
    def __init__(self, message='',status_code=None,payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload
    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        rv['status'] = self.status
        return rv
class EmptyException(Exception):
    status_code = 400
    status = False
    def __init__(self, message='',status_code=None,payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload
    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        rv['status'] = self.status
        return rv

class NotValidException(Exception):
    status_code = 400
    status = False
    def __init__(self, message='',status_code=None,payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload
    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        rv['status'] = self.status
        return rv

class ExpiredException(Exception):
    status_code = 400
    status = False
    def __init__(self, message='',status_code=None,payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload
    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        rv['status'] = self.status
        return rv

