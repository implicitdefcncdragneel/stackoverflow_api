import requests
from api.tasks import searchtask, answertask

class GetStackExchange:

    EP = 'https://api.stackexchange.com/2.3/{}'  

    def get_all_questions(self, page, order="desc", sort="activity", site="stackoverflow"):
        param={
            "page": page,
            "order": order,
            "sort" : sort,
            "site" : "stackoverflow"
        }
        try:
            response = requests.get(self.EP.format('questions'), params=param)
            json_response = response.json()
            return json_response
        except Exception as err:
            print(f'Other error occurred: {err}')


    def search(self, page, tagged, order="desc", sort="activity", site="stackoverflow"):
        param={
            "tagged" : "python",
            "page": page,
            "order": order,
            "sort" : sort,
            "site" : "stackoverflow"
        }
        try:
            response = requests.get(self.EP.format('search'), params=param)
            json_response = response.json()
            searchtask.delay(tagged,json_response)
            return json_response
        except Exception as err:
            print(f'Other error occurred: {err}')

    def advanceSearch(self, q, page, order="desc", sort="activity", site="stackoverflow"):
        param={
            "q": q,
            "page": page,
            "order": order,
            "sort" : sort,
            "site" : "stackoverflow"
        }
        try:
            response = requests.get(self.EP.format('search/advanced'), params=param)
            json_response = response.json()
            searchtask.delay(q,json_response)
            return json_response
        except Exception as err:
            print(f'Other error occurred: {err}')

    def answer(self,question_id, order="desc", sort="activity", site="stackoverflow"):
        param={
            "question_id": question_id,
            "order": order,
            "sort" : sort,
            "site" : "stackoverflow"
        }
        try:
            response = requests.get(self.EP.format('questions/'+str(question_id)+'/answers'), params=param)
            json_response = response.json()
            answertask.delay(question_id,json_response)
            return response.json()
        except Exception as err:
            print(f'Other error occurred: {err}')