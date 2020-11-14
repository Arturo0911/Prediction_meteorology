import torch
import pandas as pd



class Process:

    def __init__(self):

        self.url_name = "https://covid19.who.int/WHO-COVID-19-global-data.csv"
        self.data_frame = pd.read_csv(self.url_name) # Read the Csv file from the url
        self.country_subset = self.data_frame[' Country'] # read and apply filters to fetch per country

        self._country_stats = None
        self._target = None
        self._new_deaths = None

        


    """
        @return dataframes for all countries
    """
    def Read(self):

        return self.data_frame
    
    def get_keys(self):

        keys_values = self.data_frame.columns
        return keys_values

    def get_country_stats(self, country):

        self._country_stats = self.data_frame[self.country_subset == country]
        


    def get_mean(self):
        
        self._target = torch.tensor(self._country_stats[[' New_cases']].values).float()


        mean_data = torch.mean(self._target, dim = 0) 
        std_data = torch.srd(self._target, dim = 0)

        return mean_data, std_data

    def get_prediction_per_country(self, country):

        pass

    def get_scatter_points(self):
        pass

    

    def get_new_cases(self):
        pass