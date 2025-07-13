import dataestructure.red_black_tree as rbt
from dataestructure.red_black_tree import INORDER_THREE_WALK_F
class Question:
    def __init__(self,id):
        self.id=id
        self.respondents= rbt.RBTree()
        self.opinion_average=None

    def insert_respondent(self,respondent):
        rbt.RB_INSERT(self.respondents,rbt.Node(
            data_object=respondent,
            keys = (respondent.opinion,respondent.experience,respondent.id)
            ))
        
    def print_info(self,attr):
        def print_respondents():
            rbt.INORDER_THREE_WALK(self.respondents,self.respondents.root,attr)
        print(f"id:{self.id}")
        print("respondents:")
        print_respondents()

    def calculate_opinion_average(self,acum=0):
        x=self.respondents.root
        def recursive_aux(x:rbt.Node,acum:int):
            if x!=self.respondents.nil:
                acum=recursive_aux(x.left,acum)
                acum+=getattr(x.object,'opinion')
                acum=recursive_aux(x.right,acum)
            return acum
            
        return recursive_aux(x,acum)/self.respondents.root.size
#Pregunta con el mayor y menor valor de moda de opiniones    
    def calculate_opinion_median(self):
        ith=self.respondents.root.size//2
        x=rbt.OS_SELECT(self.respondents.root,ith)
        return getattr(x.object,'opinion')
    

    def calculate_opinion_mode(self):
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

        INORDER_THREE_WALK_F(self.respondents, self.respondents.root, contar_opinion)
        return modes

"""
funcion para hallar el mayor consenso

Hallar la pregunta con mayor moda,
hallar la cantidad de encuestados de la pregunta con mayor moda 
hacer un contador para hallar los encuestados totales
"""



        
            
