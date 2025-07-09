import dataestructure.red_black_three as rbt

class Question:
    def __init__(self,id):
        self.id=id
        self.respondents= rbt.RBThree(rbt.NIL)
    def insert_respondents(self,respondent):
        rbt.RB_INSERT(self.respondents,rbt.Node(
            object=respondent,
            key_primary_attr='opinion',
            key_secondary_attr='experience',
            key_third_attr='id'
            ))
