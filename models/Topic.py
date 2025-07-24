import models.Question as qt
import math
import dataestructure.red_black_tree as rbt

class Topic:
    def __init__(self,id:int):
        self.id=id
        self.questions=rbt.RBTree()

    def insert_question(self,question:qt.Question):
        rbt.RB_INSERT(self.questions,rbt.Node(
            data_object=question,
            keys=(
            rbt.TREE_AVERAGE_ATTR(question.respondents,question.respondents.root,lambda x:getattr(x.object,'opinion')),
            rbt.TREE_AVERAGE_ATTR(question.respondents,question.respondents.root,lambda x:getattr(x.object,'experience')),
            question.respondents.root.size
            )
        ))
    
    def get_info(self):
        
        avg_op_questions= rbt.TREE_AVERAGE_ATTR(self.questions,self.questions.root,
                                                lambda node_q:node_q.object.calculate_average_opinion()['attr']
                                                )
        return f"[{avg_op_questions:.2f}] Tema {self.id}:\n"
    
    
    def max_median_question(self):
        return rbt.MAX_GENERIC_QUESTION_ATTR(
            self.questions,
            lambda node: getattr(node.object,'calculate_opinion_median')()

            )
    
    def min_median_question(self):
        return rbt.MIN_GENERIC_QUESTION_ATTR(
            self.questions,
            lambda node: getattr(node.object,'calculate_opinion_median')()

            )

    def max_mode_question(self):
        return rbt.MAX_GENERIC_QUESTION_ATTR(
            self.questions,
            lambda node: node.object.calculate_opinion_mode_consensus('mode')

            )
    
    def min_mode_question(self):
        return rbt.MIN_GENERIC_QUESTION_ATTR(
            self.questions,
            lambda node: node.object.calculate_opinion_mode_consensus('mode')

            )

    def max_consensus_question(self):
        return rbt.MAX_GENERIC_QUESTION_ATTR(
            self.questions,
            lambda node: node.object.calculate_opinion_mode_consensus('concensus')

            )
    
    def min_consensus_question(self):
        return rbt.MIN_GENERIC_QUESTION_ATTR(
            self.questions,
            lambda node: node.object.calculate_opinion_mode_consensus('concensus')

            )
        

    
    def max_opinion_avg_question(self):
        return rbt.MAX_GENERIC_QUESTION_ATTR(
            self.questions,
            lambda node: node.object.calculate_average_opinion()

            )
    
    def min_opinion_avg_question(self):
        return rbt.MIN_GENERIC_QUESTION_ATTR(
            self.questions,
            lambda node: node.object.calculate_average_opinion()

            )
    
    def max_opinion_extremism(self):
        return rbt.MAX_GENERIC_QUESTION_ATTR(
            self.questions,
            lambda node: node.object.calculate_opinion_extremism()

            )

    
    def num_respondents(self):
        state={"count":0,}
        
        def num_respondents_by_question(question:rbt.Node,state:dict):
            state['count']+= question.object.respondents.root.size

        rbt.INORDER_THREE_WALK_GENERIC(self.questions,self.questions.root,num_respondents_by_question,state)
        
        return state['count']
    


