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
    
    def print_questions(self):
        def print_node(node:rbt.Node):
            print(getattr(node.object,'id'))

        rbt.INORDER_THREE_WALK_GENERIC(self.questions,self.questions.root,print_node)
    
    
    def max_median_question(self):
        state={
            'question_max':None,
            'max_median':-math.inf
        }
        
        def max_question(node:rbt.Node,state:dict[str,any]):
            
            median=getattr(node.object,'calculate_opinion_median')()
            if median>state['max_median']:
                state['max_median']=median
                state['question_max']=node.object

            
        rbt.INORDER_THREE_WALK_GENERIC(self.questions,self.questions.root,max_question,state)
        return state
        

    def max_mode_question(self):
        state={
            'question_max':None,
            'max_mode':-math.inf
        }
        
        def max_question(node:rbt.Node,state:dict[str,any]):
            mode=getattr(node.object,'calculate_opinion_mode')()
            if mode>state['max_mode']:
                state['max_mode']=mode
                state['question_max']=node.object

            
        rbt.INORDER_THREE_WALK_GENERIC(self.questions,self.questions.root,max_question,state)
        return state
    
    def max_consensus_question(self):
        state={
            'question_max':None,
            'max_consensus':-math.inf
        }
        
        def max_consensus(node:rbt.Node,state:dict[str,any]):
            mode,consensus = getattr(node.object,'calculate_opinion_mode_consensus')()
            if consensus>state['max_consensus']:
                state['max_consensus']=consensus
                state['question_max']=node.object

            
        rbt.INORDER_THREE_WALK_GENERIC(self.questions,self.questions.root,max_consensus,state)
        return state
    
    def max_opinion_avg_question(self):
        state={
            'question_max':None,
            'max_opinion_avg':-math.inf
        }
        
        def max_opinion_avg(node:rbt.Node,state:dict[str,any]):
            op_avg = getattr(node.object,'calculate_average_opinion')()
            if op_avg>state['max_opinion_avg']:
                state['max_opinion_avg']=op_avg
                state['question_max']=node.object

            
        rbt.INORDER_THREE_WALK_GENERIC(self.questions,self.questions.root,max_opinion_avg,state)
        return state

    
    def num_respondents(self):
        state={"count":0}
        
        def num_respondents_by_question(question:rbt.Node,state:dict):
            state['count']+= question.object.respondents.root.size

        rbt.INORDER_THREE_WALK_GENERIC(self.questions,self.questions.root,num_respondents_by_question,state)
        
        return state['count']
    


