import sys
import os
import re

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
        file_path = self.path  # Replace with your file's path

        try:
            with open(file_path, 'r', encoding="utf-8") as file:
                content=file.read()
            
            raw_blocks=re.split(r"\n{2,}",content.strip())
            
            respondents=[]
            topics=[]

            for line in raw_blocks[0].splitlines():
                match=re.match(r"^(.*),\s*Experticia:\s*(\d+),\s*Opinión:\s*(\d+)",line)
                if match:
                    respondents.append({
                        "name":match.group(1).strip(),
                        "experience":int(match.group(2)),
                        "opinion":int(match.group(3))
                    })
            # print(respondents)
            topics=[]
            for block in raw_blocks[1:]:
                topic=[]
                for line in block.strip().splitlines():
                    # print(tuple(map(int,re.findall(r"\d+",line))))
                    topic.append(tuple(map(int,re.findall(r"\d+",line))))
                if topic:
                    topics.append(topic)
            

            self.survey=sv.Survey(1)
            for t in range(len(topics)) :
                topic_obj=tp.Topic(t+1)
                for q in range(len(topics[t])):
                    question=qt.Question(q+1,t+1)
                    for id in topics[t][q]:
                        
                        respondent=respondents[id-1]
                        question.insert_respondent(rp.Respondent(
                            respondent['name'],
                            respondent['opinion'],
                            respondent['experience'],
                            id
                        ))
                    topic_obj.insert_question(question)
                self.survey.insert_topic(topic_obj)
                    
        except FileNotFoundError:
            print(f"Error: The file '{file_path}' was not found.")
        except Exception as e:
            print(f"An error occurred: {e}")
          

    def expected_out(self):
        return self.survey.get_info()

    def get_respondents(self):
        return self.survey.get_list_respondents()

    def max_median_question(self):
        return self.survey.max_median_question()

    def min_median_question(self):
        return self.survey.min_median_question()
    
    def max_concensus_question(self):
        return self.survey.max_consensus_question()

    def min_concensus_question(self):
        return self.survey.min_consensus_question()

    def max_mode_question(self):
        return self.survey.max_mode_question()
    
    def min_mode_question(self):
        return self.survey.min_mode_question()

    def max_opinion_avg_question(self):
        return self.survey.max_opinion_avg_question()

    def min_opinion_avg_question(self):
        return self.survey.min_opinion_avg_question()
    
    def max_opinion_extremism(self):
        return self.survey.max_opinion_extremism()
    
    
    
    


        

        





    
