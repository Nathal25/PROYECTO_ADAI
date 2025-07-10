import dataestructure.red_black_three as rbt

class Question:
    def __init__(self,id):
        self.id=id
        self.respondents= rbt.RBThree()
        self.opinion_average=None
    def insert_respondent(self,respondent):
        rbt.RB_INSERT(self.respondents,rbt.Node(
            data_object=respondent,
            key_primary_attr='opinion',
            key_secondary_attr='experience',
            key_third_attr='id'
            ))
    def print_info(self,attr):
        def print_respondents():
            rbt.INORDER_THREE_WALK(self.respondents,self.respondents.root,attr)
        print(f"id:{self.id}")
        print("respondents:")
        print_respondents()

    def calculate_opinion_average(self,acum=0):
        x=self.respondents.root
        def recursive_aux(x,acum):
            if x!=self.respondents.nil:
                acum=recursive_aux(x.left,acum)
                acum+=getattr(x.object,'opinion')
                acum=recursive_aux(x.right,acum)
            return acum
            
        return recursive_aux(x,acum)/self.respondents.root.size
        
            
