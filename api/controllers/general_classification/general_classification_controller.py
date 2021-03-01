from flask import Blueprint
from flask import request
from flask import jsonify
from api.services.classification_service import ClassificationModel
import numpy as np


general_classification_bp = Blueprint('general_classification_bp', __name__)

# Services
model_service = ClassificationModel()
print('Call to initialize classification model')

@general_classification_bp.route('/classify_trx', methods=['POST'])
def classify_trx():
    # get the body of the request
    trx_data = request.get_json()

    # run the classification ml model
    classified_trx = model_service.classify_transactions(trx_data)

    # return classified data
    return jsonify(classified_trx)
