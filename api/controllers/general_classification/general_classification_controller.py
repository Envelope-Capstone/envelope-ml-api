from flask import Blueprint
from flask import request
from flask import jsonify
from api.services.data_preprocessing_service import DataPreproccessingService
import pandas as pd


general_classification_bp = Blueprint('general_classification_bp', __name__)

# Services
preprocessing_service = DataPreproccessingService()

@general_classification_bp.route('/classify_trx', methods=['POST'])
def classify_trx():
    # get the body of the request
    trx_content = request.get_json()
    # Convert it to a DF
    df = pd.DataFrame(trx_content)
    # Clean the data
    unp_df = preprocessing_service.clean_data()

    # return classified data
    return jsonify(unp_df)
