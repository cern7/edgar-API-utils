import pandas as pd

class CompanyFacts:
    def __init__(self, entity_name):
        self.entity_name = entity_name
        self.facts_by_year = {}

    def add_fact(self, year, tag, value):
        if year not in self.facts_by_year:
            self.facts_by_year[year] = {}
        self.facts_by_year[year][tag] = value
        
    def get_fact(self, year, tag):
            return self.facts_by_year.get(year, {}).get(tag, None)
    
    def get_all_facts(self):
        return self.facts_by_year
        
    def to_dataFrame(self):
            return pd.DataFrame.from_dict(self.facts_by_year, orient='index').reset_index().rename(columns={'index': 'Year'})
        
    def __repr__(self):
        return f"CompanyFacts(entity_name={self.entity_name}, facts_by_year={self.facts_by_year})"