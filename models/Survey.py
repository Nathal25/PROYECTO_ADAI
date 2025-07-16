import dataestructure.red_black_tree as rbt
import models.Topic as tp
import math

class Survey:
    def __init__(self,id):
        self.name=id
        self.topics=rbt.RBTree()

    def insert_topic(self,topic:tp.Topic):
        rbt.RB_INSERT(self.topics,rbt.Node(
            data_object=topic,
            keys=(
                rbt.TREE_AVERAGE_ATTR(
                    topic.questions,
                    topic.questions.root,
                    lambda question: rbt.TREE_AVERAGE_ATTR(
                        question.object.respondents,
                        question.object.respondents.root,
                        lambda respondent: getattr(respondent.object,'opinion'))
                ),
                rbt.TREE_AVERAGE_ATTR(
                    topic.questions,
                    topic.questions.root,
                    lambda question: rbt.TREE_AVERAGE_ATTR(
                        question.object.respondents,
                        question.object.respondents.root,
                        lambda respondent: getattr(respondent.object,'experience'))
                ),
                topic.num_respondents()
            )
        ))

        
    def print_topics(self):
        def print_node(node:rbt.Node):
            print(getattr(node.object,'id'))

        rbt.INORDER_THREE_WALK_GENERIC(self.topics,self.topics.root,print_node)

    
    def max_median_question(self):
        return rbt.MAX_GENERIC_QUESTION_ATTR(
            self.topics,
            lambda node: node.object.max_median_question()

            )
    
    def min_median_question(self):
        return rbt.MIN_GENERIC_QUESTION_ATTR(
            self.topics,
            lambda node: node.object.min_median_question()

            )
    

    def max_consensus_question(self):
        return rbt.MAX_GENERIC_QUESTION_ATTR(
            self.topics,
            lambda node: node.object.max_consensus_question()

            )
    
    def min_consensus_question(self):
        return rbt.MIN_GENERIC_QUESTION_ATTR(
            self.topics,
            lambda node: node.object.min_consensus_question()

            )
    
    def max_mode_question(self):
        return rbt.MAX_GENERIC_QUESTION_ATTR(
            self.topics,
            lambda node: node.object.max_mode_question()

            )
    def min_mode_question(self):
        return rbt.MIN_GENERIC_QUESTION_ATTR(
            self.topics,
            lambda node: node.object.min_mode_question()

            )
    
    
    
    def max_opinion_avg_question(self):
        
        return rbt.MAX_GENERIC_QUESTION_ATTR(
            self.topics,
            lambda node: node.object.max_opinion_avg_question()
        )
        

    def min_opinion_avg_question(self):
        
        return rbt.MIN_GENERIC_QUESTION_ATTR(
            self.topics,
            lambda node: node.object.min_opinion_avg_question()
        )
        


