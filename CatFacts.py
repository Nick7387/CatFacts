import requests

class CatFacts:

    def __init__(self):

        """api позволяет получать непосредственно факты о животных 
        и иформацию о корневом пользователе
        
        --------------------------------------
        РАБОТА С ФАКТАМИ
        
        Получить факты можно тремя способами: случайный факт, факт по его id, мои факты.
        заголовок - random
        заголовок - id
        заголовок - me
        
        заголовок - random
            facts_random()
            выдает один факт случайно в формате str
            
            
            facts_random_filter(animals,amount)
            Метод выдает факты о кокретном животном animals в количестве amount ответов
            
            animals: ['cat','dog','snail','horse'] 
            amount:  максимум 500 фактов
            
            Пример: facts_random_filter(['cat','dog'], 200)
            Метод выдает данные в формате json
            
        заголовок - id
            facts_id()
                        
        заголовок - me
            facts_me()
        
        
        -------------------------------------
        ИНФОРМАЦИЯ О ПОЛЬЗОВАТЕЛЕ 
        
        Получить информацию о пользователе можно с помощью заголовка users/me
        расположен в словаре self.users_headers
        запрос реализуется функцией:
            
        current_user_get_info() - метод возвращает данные в формате json
        
        """
        self.base_url = "https://cat-fact.herokuapp.com/"
        
        self.base_headers  = {'facts': 'facts', 'users': 'users/me'}
        self.facts_headers = {'random': 'facts/random','id': 'facts/'+str(id),'me': 'facts/me'} 
        self.facts_random_headers = {'random': 'facts/random'} 
        self.users_headers = {'me': 'users/me'}

    def facts_random(self):
        self.res = requests.get(self.base_url, headers=self.base_headers['users'])
        if self.res:
            print('find_facts_random.Response OK: ', self.res.status_code)
            self.facts=self.res.json().get('text')
            return self.facts
        else:
            print('find_facts_random.Response Failed: ', self.res.status_code)
            return []

    def facts_random_filter(self,animals,amount):
        url=self.base_url + self.facts_headers['random']
        animals_data=','.join(animals)
        params = {'animal_type':animals_data, 'amount':amount}
        self.res = requests.get(url, params=params)
        print(self.res.url)
        if self.res:
            print('find_facts_random_filter.Response OK: ', self.res.status_code)
            self.facts=self.res.json()              
            return self.facts
        else:
            print('find_facts_random_filter.Response Failed: ', self.res.status_code)
            return False
            
    def facts_id(self):
        return self
    
    def facts_me(self):
        return self
            
    def current_user_get_info(self):
        self.base_url = "https://cat-fact.herokuapp.com"
        self.res = requests.get(self.base_url, headers=self.base_headers['users'])
        self.me_info=self.res.json()
        return self.me_info

