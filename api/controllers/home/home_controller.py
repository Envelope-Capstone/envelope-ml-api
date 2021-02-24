from flask import Blueprint
from flask import current_app

home_bp = Blueprint('home_bp', __name__)

@home_bp.route('/', methods=['GET'])
def show_home():
    return 'ML API is running!'
