from typing import Callable,Any
import math

RED='RED'
BLACK='BLACK'

class Node():
    def __init__(self,data_object:object=None,keys:tuple=()):
        self.color=BLACK
        self.left=None
        self.right=None
        self.parent=None
        self.object=data_object
        self.size=1
        self.key=keys


NIL=Node()
NIL.parent=NIL
NIL.right=NIL
NIL.left=NIL
NIL.size=0   
    
class RBTree:

    def __init__(self,root:Node=NIL):
        self.root=root
        self.nil=NIL
    
def LEFT_ROTATE(T:RBTree,x:Node):
    y=x.right
    x.right=y.left
    if y.left!=T.nil:
        y.left.parent=x
    y.parent=x.parent
    if x.parent==T.nil:
        T.root=y
    elif x==x.parent.left:
        x.parent.left=y
    else:
        x.parent.right=y
    y.left=x
    x.parent=y
    y.size=x.size
    x.size=x.left.size + x.right.size + 1
    

def RIGHT_ROTATE(T:RBTree,x:Node):
    y=x.left
    x.left=y.right
    if y.right!= T.nil:
        y.right.parent=x
    y.parent=x.parent
    if x.parent==T.nil:
        T.root=y
    elif x==x.parent.right:
        x.parent.right=y
    else:
        x.parent.left=y
    y.right=x
    x.parent=y
    y.size=x.size
    x.size=x.left.size + x.right.size + 1


def RB_INSERT_FIXUP(T:RBTree,z:Node):
    while z.parent.color==RED:
        # case: parent is left child
        if z.parent==z.parent.parent.left:
            y=z.parent.parent.right
            if y.color==RED:
                #case 1: Uncle  is red - recolor
                z.parent.color=BLACK
                y.color=BLACK
                z.parent.parent.color=RED
                z=z.parent.parent
            else:
                #Case 2: z is right child-rotate left
                if z==z.parent.right:
                    z=z.parent
                    LEFT_ROTATE(T,z)
                #Case 3: z is left child - rotate right
                z.parent.color=BLACK
                z.parent.parent.color=RED
                RIGHT_ROTATE(T,z.parent.parent)
        else:
            #symetric case
            y=z.parent.parent.left
            if y.color==RED:
                z.parent.color=BLACK
                y.color=BLACK
                z.parent.parent.color=RED
                z=z.parent.parent
            else:
                if z==z.parent.left:
                    z=z.parent
                    RIGHT_ROTATE(T,z)
                z.parent.color=BLACK
                z.parent.parent.color=RED
                LEFT_ROTATE(T,z.parent.parent)
    T.root.color=BLACK #root always be black
                    
def RB_INSERT(T:RBTree,z:Node):
    y=T.nil
    x=T.root
    while x!=T.nil:
        y=x
        y.size+=1   
        if z.key<x.key:
            x=x.left          
        else:
            x=x.right
    z.parent=y
    if y==T.nil:
        T.root=z
    elif z.key<y.key:
        y.left=z
    else:
        y.right=z    
    z.left=T.nil
    z.right=T.nil
    z.color=RED
    RB_INSERT_FIXUP(T,z)

#binary search three methods

def INORDER_THREE_WALK_GENERIC(T: RBTree, x: Node, body: Callable, *args, **kwargs):
    if x != T.nil:
        INORDER_THREE_WALK_GENERIC(T, x.left, body, *args, **kwargs)
        body(x, *args, **kwargs)  
        INORDER_THREE_WALK_GENERIC(T, x.right, body, *args, **kwargs)

def INORDER_THREE_WALK_GENERIC_REVERSE(T: RBTree, x: Node, body: Callable, *args, **kwargs):
    if x != T.nil:
        INORDER_THREE_WALK_GENERIC_REVERSE(T, x.right, body, *args, **kwargs)
        body(x, *args, **kwargs)  
        INORDER_THREE_WALK_GENERIC_REVERSE(T, x.left, body, *args, **kwargs)





def TREE_AVERAGE_ATTR(T:RBTree,x:Node,f:Callable,*args,**kwargs):
    
    def recursive_aux(x:Node):
        if x==T.nil:
            return 0.0
        left_sum=recursive_aux(x.left)
        node_value=f(x,*args,**kwargs)
        right_sum=recursive_aux(x.right)
        return left_sum + right_sum + node_value 
        
    return recursive_aux(x)/x.size if x.size > 0 else 0.0 


def MAX_GENERIC_QUESTION_ATTR(tree:RBTree,f:Callable,*args,**kwargs):
    state={
        'question':None,
        'attr':-math.inf
    }
        
    def max_generic_aux(node:Node,state:dict[str,Any],f:Callable,*args,**kwargs):
        result=f(node,*args,**kwargs)
        if result['attr']>state['attr']:
            state['attr']=result['attr']
            state['question']=result['question']
        elif result['attr']==state['attr']:
            if state['question'] is None or result['question'].topic_id<state['question'].topic_id:
                state['question']=result['question']
            elif result['question'].id<state['question'].id:
                state['question']=result['question']


    
    INORDER_THREE_WALK_GENERIC(tree,tree.root,max_generic_aux,state,f,*args,**kwargs)
    return state


def MIN_GENERIC_QUESTION_ATTR(tree:RBTree,f:Callable,*args,**kwargs):
    state={
        'question':None,
        'attr':math.inf
    }
        
    def min_generic_aux(node:Node,state:dict[str,Any],f:Callable,*args,**kwargs):
        result=f(node,*args,**kwargs)
        if result['attr']<state['attr']:
            state['attr']=result['attr']
            state['question']=result['question']

        elif result['attr']==state['attr']:
            if state['question'] is None or result['question'].topic_id<state['question'].topic_id:
                state['question']=result['question']
            elif result['question'].id<state['question'].id:
                state['question']=result['question']
    
    INORDER_THREE_WALK_GENERIC(tree,tree.root,min_generic_aux,state,f,*args,**kwargs)
    return state

#statistics orders

def OS_SELECT(x:Node,i:int):
    r=x.left.size + 1
    if i==r:
        return x
    elif i<r:
        return OS_SELECT(x.left,i)
    else:
        return OS_SELECT(x.right,i-r)

