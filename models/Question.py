import dataestructure.red_black_tree as rbt
from dataestructure.red_black_tree import INORDER_THREE_WALK_GENERIC, INORDER_THREE_WALK_GENERIC_REVERSE
class Question:
    def __init__(self,id,topic_id=None):
        self.id=id
        self.topic_id=topic_id
        self.respondents= rbt.RBTree()

    def insert_respondent(self,respondent):
        rbt.RB_INSERT(self.respondents,rbt.Node(
            data_object=respondent,
            keys = (respondent.opinion,respondent.experience,respondent.id)
            ))
        
    def get_info(self):
        string=""
        def add_string(node):
            nonlocal string
            string+=str(node.object.id)+","
        
        rbt.INORDER_THREE_WALK_GENERIC_REVERSE(self.respondents,self.respondents.root,add_string)
        
        return f"    [{self.calculate_average_opinion()['attr']:.2f}] Pregunta{self.topic_id}.{self.id}:({string.rstrip(',')})\n"


   
    # def calculate_opinion_median(self):
    #     ith=self.respondents.root.size//2
    #     x=rbt.OS_SELECT(self.respondents.root,ith)
    #     return {
    #         'attr':getattr(x.object,'opinion'),
    #         'question':self
    #         } 

    def calculate_opinion_median(self):
        size = self.respondents.root.size
        if size == 0:
            return None  # Handle empty tree case
        if size % 2 == 0:
            # Even number of respondents, select the lower of the two middle nodes
            ith = size // 2
        else:
            # Odd number of respondents, select the middle node
            ith = (size + 1) // 2
        x = rbt.OS_SELECT(self.respondents.root, ith)
        return {
            'attr': getattr(x.object, 'opinion'),
            'question': self
        }                  
    

    def calculate_opinion_mode_consensus(self,attr):
        prev = [None]
        count = [0]
        max_count = [0]
        modes = []

        def contar_opinion(node):
            opinion = getattr(node.object, 'opinion')

            if prev[0] == opinion:
                count[0] += 1
            else:
                count[0] = 1

            if count[0] > max_count[0]:
                max_count[0] = count[0]
                modes.clear()
                modes.append(opinion)
            elif count[0] == max_count[0]:
                if opinion not in modes:
                    modes.append(opinion)

            prev[0] = opinion

        INORDER_THREE_WALK_GENERIC(self.respondents, self.respondents.root, contar_opinion)
        results= (modes[0],max_count[0]/self.respondents.root.size)

        if attr=='mode': return {'attr':results[0],'question':self} 
        else: return {'attr':results[1],'question':self}

    #funcion para hallar el promedio de opiniones
    def calculate_average_opinion(self):
        total_opinion = 0
        count = 0

        def sumar_opinion(node):
            nonlocal total_opinion, count
            opinion = getattr(node.object, 'opinion')
            total_opinion += opinion
            count += 1

        INORDER_THREE_WALK_GENERIC(self.respondents, self.respondents.root, sumar_opinion)

        if count == 0:
            return {'attr':0,'question':self}
        return {'attr':total_opinion / count,'question':self}

    def calculate_opinion_extremism(self):
        count=0
        def extremism_aux(node):
            nonlocal count
            opinion=node.object.opinion
            if opinion==10 or opinion==0:
                count+=1

        INORDER_THREE_WALK_GENERIC(self.respondents,self.respondents.root,extremism_aux)

        return {'attr':count/self.respondents.root.size,'question':self}   
    
    
            




"""
funcion para hallar el mayor consenso

Hallar la pregunta con mayor moda,
hallar la cantidad de encuestados de la pregunta con mayor moda 
hacer un contador para hallar los encuestados totales
"""



        
            
