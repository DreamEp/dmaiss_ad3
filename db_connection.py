import json 
from firebase import firebase
from numpy.core.fromnumeric import nonzero
import pandas as pd

class FireConnection():
    
    def __init__(self):
        self.db = firebase.FirebaseApplication("https://dmaiss-ad3-onlinedb.firebaseio.com/", None)

    def get_data(self):
        query = self.db.get('/answers/', None)
        if query is None:
            return []
        else:
            return pd.DataFrame.from_dict(query, orient='index').reset_index(drop=True)

    def get_quizz(self):
        query = self.db.get('/quizz/', None)
        return query[list(query.keys())[-1]] # get last quizz version

    def add_answers(self, answers):
        self.db.post('/answers/', answers)

    def update_quizz(self, quizz):
        self.db.post('/quizz/', quizz)


    def _setup(self): # Obsolete, db is now set-up
        # Upload quizz for the first time
        # self.db.delete('/', None)
        self.db.post('/quizz/', json.load(open('quizz.json')))
        print(self.get_quizz())

# FireConnection()._setup()