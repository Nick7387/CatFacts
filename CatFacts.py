import requests

class CatFacts:

    def __init__(self):
        self.base_url = "https://cat-fact.herokuapp.com/facts/"

    def find_facts_random(self):
        self.res = requests.get(self.base_url+'random/')
        if self.res:
            print('find_facts_random.Response OK: ', self.res.status_code)
            self.facts=self.res.json().get('text')
            return self.facts
        else:
            print('find_facts_random.Response Failed: ', self.res.status_code)
            return []

    def find_facts_random_filter(self,animals,amount):
            animals_data=','.join(animals)
            params = {'animal_type':animals_data, 'amount':amount}
            self.res = requests.get(self.base_url+'random',params=params)
            if self.res:
                print('find_facts_random_filter.Response OK: ', self.res.status_code)
                
                self.facts=[]
                self.users=[]
                self.dict_data = {}
                
                for i in self.res.json():
                    self.facts.append(i.get('text'))
                    self.users.append(i.get('user'))
                    
                    if len(self.facts)>0:
                        
                        for i in range(len(self.facts)):
                            self.dict_data[self.users[i]] = self.facts[i]
                    
                return self.dict_data
            else:
                print('find_facts_random_filter.Response Failed: ', self.res.status_code)
                return []

