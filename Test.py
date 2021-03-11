import requests
from CatFacts import CatFacts

animals=['cat','dog','snail','horse']
amount=500



def test_all_facts(animals, amount):
    cat_facts_data = CatFacts()
    #print(len(cat_facts_data.find_facts_random_filter(animals, amount)))
    for i in animals:
        a=cat_facts_data.find_facts_random_filter([i], amount)
        return a
    
b=test_all_facts(animals, amount)