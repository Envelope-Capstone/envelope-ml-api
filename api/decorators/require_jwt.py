from functools import wraps
from flask import request

def require_jwt(controller_func):
    @wraps(controller_func)
    def wrap(*args, **kwargs):
        auth_token = request.headers['Authorization']
        print(auth_token)
        return controller_func(*args, **kwargs)
    return wrap