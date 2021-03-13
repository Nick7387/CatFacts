import requests
from CatFacts import CatFacts

animals=['cat','dog','snail','horse']
amount=300



def test_all_facts(animals, amount):
    cat_facts_data = CatFacts()
    #print(len(cat_facts_data.find_facts_random_filter(animals, amount)))
    return cat_facts_data.facts_random_filter(animals, amount)
    # for i in animals:
    #     a=cat_facts_data.find_facts_random_filter([i], amount)
    #     return a
    
b=test_all_facts(animals, amount)
users=[]
for i in range(len(b)):
    users.append(b[i]['user'])

uniqNames = sorted(set(users)) #remove duplicate words and sort
d = {}    

for name in uniqNames:
    d[name] = users.count(name) 
    
print(d)
    
s=list(d.items())