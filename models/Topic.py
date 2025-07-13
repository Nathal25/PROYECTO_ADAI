from dataestructure.red_black_tree import INORDER_THREE_WALK_F
import dataestructure.red_black_tree as rbt
class Topic:
    def __init__(self,questions,id):
        self.id=id
        self.questions=questions

    def insert_question(self,question):
        rbt.RB_INSERT(self.respondents,rbt.Node(
            data_object=question,
            key_primary_attr='opinion',
            key_secondary_attr='experience',
            key_third_attr='id'
            ))

    def consenso(self):
        totalEncuestados = 0

