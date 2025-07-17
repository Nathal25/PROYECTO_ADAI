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
    
    
    def print_info(self):

        def print_expected_out(node_t:rbt.Node):
            topic=node_t.object
            topic.print_info()
            rbt.INORDER_THREE_WALK_GENERIC_REVERSE(
                topic.questions,
                topic.questions.root,
                lambda node_q: node_q.object.print_info()
                )
        
        rbt.INORDER_THREE_WALK_GENERIC_REVERSE(
            self.topics,
            self.topics.root,
            print_expected_out
        )
                                               
                                               

    
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
    
    def max_opinion_extremism(self):
        return rbt.MAX_GENERIC_QUESTION_ATTR(
            self.topics,
            lambda node: node.object.max_opinion_extremism()

            )
    
    def print_list_respondents(self):
        aux_tree=rbt.RBTree()

        rbt.INORDER_THREE_WALK_GENERIC(
            self.topics,
            self.topics.root,
            lambda node_topic: rbt.INORDER_THREE_WALK_GENERIC(
                node_topic.object.questions,
                node_topic.object.questions.root,
                lambda node_question: rbt.INORDER_THREE_WALK_GENERIC(
                    node_question.object.respondents,
                    node_question.object.respondents.root,
                    lambda node_respondent: rbt.RB_INSERT(aux_tree,rbt.Node(
                        data_object=node_respondent.object,
                        keys=(node_respondent.object.experience,node_respondent.object.id)
                    ))

                )
            
            )
        )

        rbt.INORDER_THREE_WALK_GENERIC_REVERSE(aux_tree,aux_tree.root,
                                               lambda node: print(
                                                   f'id: {node.object.id},name:{node.object.name}, opinion: {node.object.opinion},expertice: {node.object.experience}'
                                               ))

        


