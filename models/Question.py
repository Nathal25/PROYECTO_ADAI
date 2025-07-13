import dataestructure.red_black_tree as rbt
import models.Respondent as rs

class Question:
    def __init__(self,id):
        self.id=id
        self.respondents= rbt.RBTree()
        

    def insert_respondent(self,respondent:rs.Respondent):
        rbt.RB_INSERT(self.respondents,rbt.Node(
            data_object=respondent,keys=
            (respondent.opinion,respondent.experience,self.id)
            ))
        
    def print_info(self,attr):
        def print_respondents(x:rbt.Node):
            print(getattr(x.object,attr))

        print(f"id:{self.id}")
        print("respondents:")
        rbt.INORDER_THREE_WALK_GENERIC(self.respondents,self.respondents.root,print_respondents)

    # def calculate_attr_average(self,acum=0,attr:str=None):
    #     x=self.respondents.root
    #     def recursive_aux(x:rbt.Node,acum:int):
    #         if x!=self.respondents.nil:
    #             acum=recursive_aux(x.left,acum)
    #             acum+=getattr(x.object,attr)
    #             acum=recursive_aux(x.right,acum)
    #         return acum
            
    #     return recursive_aux(x,acum)/self.respondents.root.size
    
    def calculate_opinion_median(self):
        ith=self.respondents.root.size//2
        x=rbt.OS_SELECT(self.respondents.root,ith)
        return getattr(x.object,'opinion')
    
    
        
            
