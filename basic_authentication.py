from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
from flask import request


from user import User


def get_password_hash(password):
    return generate_password_hash(password)


def verify_password(email, password):
    user = None
    
    return user is not None and check_password_hash(user.password, password)

    
def require_login(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        token = request.headers.get('token')
        if not token or not User.verify_token(token):
            return "Forbidden", 403
        return func(User.verify_token(token), *args, **kwargs)
    return wrapper
