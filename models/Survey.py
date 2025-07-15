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
        state={
            "max_median":-math.inf,
            "question_max":None
            }
        def max_median_question_by_topic(node_topic:rbt.Node,state:dict):
            median= node_topic.object.max_median_question()
            if median['max_median'] > state['max_median']:
                state['max_median']=median['max_median']
                state['question_max']=median['question_max']
        rbt.INORDER_THREE_WALK_GENERIC(self.topics,self.topics.root,max_median_question_by_topic,state)
        return state
    
    def max_mode_question(self):
        state={
            "max_mode":-math.inf,
            "question_max":None
            }
        def max_mode_question_by_topic(node_topic:rbt.Node,state:dict):
            mode= node_topic.object.max_mode_question()
            if mode['max_mode'] > state['max_mode']:
                state['max_mode']=mode['max_mode']
                state['question_max']=mode['question_max']
        rbt.INORDER_THREE_WALK_GENERIC(self.topics,self.topics.root,max_mode_question_by_topic,state)
        return state
    
    def max_mode_question_consensus(self):
        state={
            "max_consensus":-math.inf,
            "question_max":None
            }
        def max_consesus_question_by_topic(node_topic:rbt.Node,state:dict):
            consensus = node_topic.object.max_consensus_question()
            if consensus['max_consensus'] > state['max_consensus']:
                state['max_consensus']=consensus['max_consensus']
                state['question_max']=consensus['question_max']
        rbt.INORDER_THREE_WALK_GENERIC(self.topics,self.topics.root,max_consesus_question_by_topic,state)
        return state
    
    def max_opinion_avg_question(self):
        state={
            "max_opinion_avg":-math.inf,
            "question_max":None
            }
        def max_opinion_avg_question_by_topic(node_topic:rbt.Node,state:dict):
            opinion_avg = node_topic.object.max_opinion_avg_question()
            if opinion_avg['max_opinion_avg'] > state['max_opinion_avg']:
                state['max_opinion_avg']=opinion_avg['max_opinion_avg']
                state['question_max']=opinion_avg['question_max']
        rbt.INORDER_THREE_WALK_GENERIC(self.topics,self.topics.root,max_opinion_avg_question_by_topic,state)
        return state

    

