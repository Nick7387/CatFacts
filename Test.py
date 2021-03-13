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
    
factsJson=test_all_facts(animals, amount) #получаем объект с именами авторов и их фактами и пр.
users=[] # задаем список имен авторов
for i in range(len(factsJson)):
    users.append(factsJson[i]['user']) # формиркем список имен авторов

uniqNames = sorted(set(users)) # формиркем список уникальных имен авторов

dictNames = {}    # создаем словарь который будет содержать в ключах уникальные имена авторов и количество фактов в значениях
for name in uniqNames:
    dictNames[name] = users.count(name) 
    
print(dictNames)
    
s=list(dictNames.items())

'''
    Вероятно поьзователь '5a9ac18c7478810ea6c06381' и есть Kasimir Schulz. =)
    
'''