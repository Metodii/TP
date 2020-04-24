from user import User
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
from flask import request
import hashlib

from itsdangerous import (
    TimedJSONWebSignatureSerializer as Serializer,
    BadSignature,
    SignatureExpired
)

SECRET_KEY = 'n1B^Ybtqp1f!E7xN@ioY#dG4H3EcX$Zyx5cLRYKoxx'


def get_password_hash(password):
    return hashlib.sha256(password.encode('utf-8')).hexdigest()

def verify_password(user, password):
    return user.password == hashlib.sha256(password.encode('utf-8')).hexdigest()

def generate_token(user):
        s = Serializer(SECRET_KEY, expires_in=2678400)
        return s.dumps({'email': user.email})

def verify_token(token):
    s = Serializer(SECRET_KEY)
    try:
        s.loads(token)
    except SignatureExpired:
        return None
    except BadSignature:
        return None
    return User.find_by_email(s.loads(token)['email'])


def require_login(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        token = request.cookies.get('token')
        if not token or not verify_token(token):
            return func(None, *args, **kwargs)
        return func(verify_token(token), *args, **kwargs)
    return wrapper
