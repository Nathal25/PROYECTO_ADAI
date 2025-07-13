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

    def max_median_question(self):
        state={
            "max_median":-math.inf,
            "max_question":None
            }
        def max_median_question_by_topic(node_topic:rbt.Node,state:dict):
            median= node_topic.object.max_median_question()
            if median['max_median'] > state['max_median']:
                state['max_median']=median['max_median']
                state['max_question']=median['max_question']
        rbt.INORDER_THREE_WALK_GENERIC(self.topics,self.topics.root,max_median_question_by_topic,state)
        return state



