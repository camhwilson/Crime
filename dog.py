
from dataclasses import dataclass


neighborhood_dict = {
    '15222' : 'Downtown/Strip District', 
    '15212' : 'Northside East',
    '15233' : 'Northside West',
    '15201' : 'Lawrenceville',
    '15214' : 'Perry',
    '15203' : 'Southside Flats',
    '15224' : 'Bloomfield',
    '15213' : 'Oakland',
    '15219' : 'The Hill',
    '15232' : 'Shadyside',
    '15217' : 'Squirrel Hill',
    '15210' : 'Allentown/Arlington',
    '15206' : 'Highland Park',
    '15211' : 'Mount Washington'
}


@dataclass
class Dog:
    
    licensetype : str
    validdate : str
    color : str
    breed : str
    zip : str
    expyear: int
    _id : int
    name : str
    
    def __post_init__(self):
        self.neighborhood = self.determine_neighborhod(self.zip)


    def determine_neighborhod (self, input):
        try:
            return neighborhood_dict[input]
        except: 
            return 'Not defined Neighborhood'
