import dataestructure.red_black_tree as rbt
from dataestructure.red_black_tree import INORDER_THREE_WALK_GENERIC
class Question:
    def __init__(self,id):
        self.id=id
        self.respondents= rbt.RBTree()

    def insert_respondent(self,respondent):
        rbt.RB_INSERT(self.respondents,rbt.Node(
            data_object=respondent,
            keys = (respondent.opinion,respondent.experience,respondent.id)
            ))
        
    def print_info(self,attr):
        def print_respondents(x:rbt.Node):
            print(getattr(x.object,attr))

        print(f"id:{self.id}")
        print("respondents:")
        rbt.INORDER_THREE_WALK_GENERIC(self.respondents,self.respondents.root,print_respondents)

   
    def calculate_opinion_median(self):
        ith=self.respondents.root.size//2
        x=rbt.OS_SELECT(self.respondents.root,ith)
        return {'max_attr':getattr(x.object,'opinion')}
    

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
        results= (modes[0],count[0]/self.respondents.root.size * 100)

        if attr=='mode': return {'max_attr':results[0]} 
        else: return {'max_attr':results[1]}

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
        return 0
    return {'max_attr':total_opinion / count}

"""
funcion para hallar el mayor consenso

Hallar la pregunta con mayor moda,
hallar la cantidad de encuestados de la pregunta con mayor moda 
hacer un contador para hallar los encuestados totales
"""



        
            
