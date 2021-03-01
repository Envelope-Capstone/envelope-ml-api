"""
This service is responsible for housing all of the machine learning models needed in the API
"""

import joblib
import re
import copy

trx_class_model = joblib.load('api/services/trx_class.pkl')
tfid = joblib.load('api/services/tfid_tokenizer.pkl')

class ClassificationModel:

    def __init__(self):
        print("initializing general classification model")

    def __remove_payment_trx(self, data):
        """
        Removes any transactions from the data that were payments to the credit/debit company. This is payment
        amounts less than 0.
        :param data: raw transaction data
        :return: list of expenses
        """
        trx_data = []
        for d in data:
            if d['Amount'] > 0:
                trx_data.append(d)
        return trx_data

    def __clean_data(self, data):
        """
        Remove any Amounts > 0
        Remove non-alpha characters from Description field
        Convert Description attribute to lower case
        :param data: json string of transactions
        :return: df of cleaned data
        """
        # clean_df = pd.DataFrame(data)
        for d in data:
            desc = d['Description'].lower()
            desc = re.sub('[^a-zA-Z]', ' ', desc)
            d['Description'] = desc
        return data

    def __encode_data_tfid(self, data):
        """
        Encode the description column of the DF with term frequency
        :param df:
        :return:
        """
        # convert description to TFID vector
        for d in data:
            desc = [d['Description']]
            d['TFID_Vec'] = tfid.transform(desc).toarray()
        return data

    def __predict(self, data, trx_data):
        """
        Predict the category for the transaction based on description TFID vector
        :param data: transaction data with TFID vector
        :param trx_data: transaction data to assign predicted category too
        :return: transaction data with new predicted category
        """
        # Loop through and predict categories for transactions passed in
        for i in range(0, len(data)):
            result = trx_class_model.predict(data[i]['TFID_Vec'])
            trx_data[i]['Category'] = result[0]
        return trx_data

    def classify_transactions(self, data):
        """
        Classifies transactions and assigns them to the proper category
        :param data: json string of transactions
        :return: dictionary of data with classified transactions
        """
        # Preprocess data
        data = self.__remove_payment_trx(data)
        trx_data = copy.deepcopy(data)
        cleaned_data = self.__clean_data(data)
        encoded_df = self.__encode_data_tfid(cleaned_data)

        # predict the classification
        trx_data = self.__predict(encoded_df, trx_data)

        return trx_data
