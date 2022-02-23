
from dataclasses import dataclass

from hashable_list import HashableList

@dataclass
class Overdose:
    
    overdose_dict: dict

    def __post_init__(self):
        self._id = self.overdose_dict['_id']
        self.death_date_and_time = self.overdose_dict['death_date_and_time']
        self.manner_of_death = self.overdose_dict['manner_of_death']
        self.age = self.overdose_dict['age']
        self.sex = self.overdose_dict['sex']
        self.race = self.overdose_dict['race']
        self.case_dispo = self.overdose_dict['case_dispo']
        
        all_ods = [self.overdose_dict['combined_od1'],
            self.overdose_dict['combined_od2'],
            self.overdose_dict['combined_od3'],
            self.overdose_dict['combined_od4'],
            self.overdose_dict['combined_od5'],
            self.overdose_dict['combined_od6'],
            self.overdose_dict['combined_od7'],
            self.overdose_dict['combined_od8'],
            self.overdose_dict['combined_od9'],
            self.overdose_dict['combined_od10']]
        
        self.drug_list = HashableList([i for i in all_ods if i is not None])

        self.incident_zip = self.overdose_dict['incident_zip']
        self.decedent_zip = self.overdose_dict['decedent_zip']
        self.case_time = self.overdose_dict['case_year']
