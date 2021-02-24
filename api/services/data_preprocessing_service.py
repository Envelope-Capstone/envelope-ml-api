import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer


class DataPreproccessingService:


    def clean_data(self, df: pd.DataFrame):
        """
        Remove any Amounts > 0
        Remove non-alpha characters from Description field
        Convert Description attribute to lower case
        :param df: dataframe of transactions
        :return: df of cleaned data
        """
        df = df.loc[df['Amount'] > 0]
        df.loc[:, 'Description'] = df.Description.str.replace('[^a-zA-Z]', ' ')
        df['Description'] = df['Description'].str.lower()
        return df

