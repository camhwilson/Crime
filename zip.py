
import pandas as pd
from dataclasses import dataclass

@dataclass
class Zip:
    
    zip : str
    dogs : list

    def __post_init__(self):
        self.dogcount = len(self.dogs)
        self.city, self.population_this_year = self.determine_city_pop()

        self.dogpercapita = self.dogs_per_capita()


        
    def determine_city_pop(self):
        namedict = {}
        popdf = pd.read_csv('zcodepopulationdata.csv')
        
        for index, row in popdf.iterrows():
            namedict[row['ZIP Code']] = (row['City'], int("".join(filter(str.isdigit, row['Population']))))
        
        try:
            return namedict[int(self.zip)]
        except: 
            return 'Not defined Zip Name', 0
    
    def dogs_per_capita(self):
        if self.population_this_year != 0: 
            return self.dogcount / self.population_this_year
