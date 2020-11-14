import torch
import pandas as pd



class Process:

    def __init__(self):

        self.url_name = "https://covid19.who.int/WHO-COVID-19-global-data.csv"
        self.data_frame = pd.read_csv(self.url_name) # Read the Csv file from the url
        self.country_subset = self.data_frame[' Country'] # read and apply filters to fetch per country

        self._country_stats = ""
        self._new_deaths = None

        
    def Read(self):

        """
            Return all dataframes
        """

        return self.data_frame
    
    def get_keys(self):

        keys_values = self.data_frame.columns
        return keys_values

    def get_country_stats(self, country):

        self._country_stats = self.data_frame[self.country_subset == country]
        

    
    # New_cases 
    def get_new_cases(self):

        # First calculate the values from the dataset
        # after that using torch methods, calculate mean and std
        # return both on int format, and using .item() to get the complete value
        
        
        _target = torch.tensor(self._country_stats[[' New_cases']].values).float()
        mean_data = int(torch.mean(_target, dim = 0).item())
        std_data = int(torch.srd(_target, dim = 0).item())

        return mean_data, std_data

    def get_new_deaths(self):
        


        _target = torch.tensor(self._country_stats[[' New_deaths']].values).float()
        mean_data = int(torch.mean(_target, dim = 0).item())
        std_data = int(torch.srd(_target, dim = 0).item())

        return mean_data, std_data

    def mortality_rate(self, mean_deaths, mean_cases):

        rate = float((mean_deaths/mean_cases)*100)

        return rate
