import sys
import os

# Agrega la ruta del proyecto al sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pandas as pd
import models.Question as qt
import models.Respondent as rp
import models.Topic as tp
import models.Survey as sv
import dataestructure.red_black_tree as rbt


class Controller:

    def __init__(self,K,M,path):
        self.K=K
        self.M=M
        self.path=path
        


    def load_data_and_validate(self):
        # '..\data_ada.csv'
        
        self.data=pd.read_csv(self.path)

        self.data.columns=self.data.columns.str.strip()

        expected_columns=['nombre','experticia','opinion','tema_id','pregunta_id','id']

        missing=[c for c in expected_columns if c not in self.data.columns]

        if missing:
            raise ValueError(f'missing columns:{missing}')

        self.topics={t+1:tp.Topic(t+1) for t in range(self.K)}
        self.questions={q+1:qt.Question(q+1) for q in range(self.M)}
        self.survey=sv.Survey(1)

    def insert_data(self):

        for _,row in self.data.iterrows():

            nombre=str(row['nombre']).strip()
            respondent=rp.Respondent(nombre,row['opinion'],row['experticia'],row['id'])

            qid=row['pregunta_id']
            tid=row['tema_id']

            if qid not in self.questions:
                raise IndexError(f'question out of range:{qid}')
            if tid not in self.topics:
                raise IndexError(f'topic out of range:{tid}')

            self.questions[qid].insert_respondent(respondent)
            self.questions[qid].topic_id=tid
            
            
        for question in self.questions.values():

            self.topics[question.topic_id].insert_question(question)

        for topic in self.topics.values():
            self.survey.insert_topic(topic)  

    def load_data_pipeline(self):
        self.load_data_and_validate()
        self.insert_data()

    def expected_out(self):
        self.survey.print_info()

        

        





    
