import torch
import pandas as pd



class Process:

    def __init__(self):
        self.url_name = "https://covid19.who.int/WHO-COVID-19-global-data.csv"
        self.data_frame = pd.read_csv(self.url_name)

    def Store(self):
        """
        docstring
        """
        pass

    def get_keys(self):

        keys_values = self.data_frame.columns

        return keys_values

    def get_prediction_per_country(self):
        pass