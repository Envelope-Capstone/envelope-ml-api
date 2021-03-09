from functools import wraps
from flask import request, abort
import json
import requests

jwt_validate_url = 'https://envelopeauthapi.azurewebsites.net/token/validate'
jwt_refresh_url = 'https://envelopeauthapi.azurewebsites.net/token/refresh'

def require_jwt(controller_func):
    @wraps(controller_func)
    def wrap(*args, **kwargs):
        # Get auth token and validate it
        auth_token = request.headers['Authorization']
        body = {'access_token': auth_token}
        validation_resp = requests.post(jwt_validate_url, json=body, headers={'Content-Type':'application/json'})
        
        # Check if status code is 401 and if so end request
        if validation_resp.status_code == 401:
            return {'message': 'User is unauthorized to access this endpoint.'}, 401

        return controller_func(*args, **kwargs)
    return wrap