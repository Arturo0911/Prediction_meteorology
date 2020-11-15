import torch
import pandas as pd



class Process:

    def __init__(self):

        self.url_name = "https://covid19.who.int/WHO-COVID-19-global-data.csv"
        self.data_frame = pd.read_csv(self.url_name) # Read the Csv file from the url
        self.country_subset = self.data_frame[' Country_code'] # read and apply filters to fetch per country

        self._country_stats = ""
        self._new_deaths = ""

        # this one is for to fetch the values, after calculate the covariance
        # to model predictions
        self.list_values = []
 
        
    def Read(self):

        """
            Return all dataframes
        """

        return self.data_frame
    
    def get_keys(self):

        keys_values = self.data_frame.columns
        return keys_values

    def get_country_stats(self, country_code):

        self._country_stats = self.data_frame[self.country_subset == country_code]
        

    
    # New_cases 
    def get_new_cases(self):

        # First calculate the values from the dataset
        # after that using torch methods, calculate mean and std
        # return both on int format, and using .item() to get the complete value
        
        
        _target = torch.tensor(self._country_stats[[' New_cases']].values).float()
        mean_data = int(torch.sum(_target, dim = 0).item())
        std_data = int(torch.std(_target, dim = 0).item())

        return mean_data, std_data

    def get_new_deaths(self):
        
        # First calculate the values from the dataset
        # after that using torch methods, calculate mean and std
        # return both on int format, and using .item() to get the complete value

        _target = torch.tensor(self._country_stats[[' New_deaths']].values).float()
        mean_data = int(torch.sum(_target, dim = 0).item())
        std_data = int(torch.std(_target, dim = 0).item())

        return mean_data, std_data

    def mortality_rate(self, mean_deaths, mean_cases):

        # Rate mortality is calculated using [(all deaths cases)/(total cases)] * (100 %)

        rate = float((mean_deaths/mean_cases)*100)

        return rate

    def _get_power_of_x_variables(self):

        # (X – X^)²


        # index into the array to calculate the covariances wth x and y's values
        list_to_index_new_cases = [] # x
        list_to_index_new_deaths = [] # y


        # X
        target_cases = torch.tensor(self._country_stats[[' New_cases']].values).float()
        mean_casses = torch.mean(target_cases, dim= 0).item()


        
        # Y
        target_deaths = torch.tensor(self._country_stats[[' New_deaths']].values).float()
        mean_deaths = torch.mean(target_deaths, dim= 0).item()

        size_of_array = len(target_cases) # size of array to load any item indexed

        suma = 0 # for the new cases
        suma_d = 0 # for death cases

        for x in target_cases:
            #print(x.item())
            list_to_index_new_cases.append(x.item() - mean_casses)
            suma += pow(x.item() - mean_casses, 2)
        
        for y in target_deaths:
            list_to_index_new_deaths.append(y.item() - mean_deaths)

        
        for z in range(0, size_of_array):
            suma_d += (list_to_index_new_cases[z] * list_to_index_new_deaths[z])



        # Beta 0 and Beta 1 has been already calculated

        y_mean = mean_deaths
        x_mean = mean_casses

        Beta1 = float(suma_d /suma)
        Beta0  = (mean_deaths - (mean_casses * Beta1))

        return y_mean, x_mean, Beta0, Beta1
        

