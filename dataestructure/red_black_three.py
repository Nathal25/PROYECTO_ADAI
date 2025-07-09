
RED='RED'
BLACK='RED'



class Node():
    def __init__(self,color:str,left:'Node',right:'Node',parent:'Node',data_object:object,key_primary_attr:str,key_secondary_attr:str,key_third_attr:str):
        self.color=color
        self.left=left
        self.right=right
        self.parent=parent
        self.object=data_object
        self.key=(
            getattr(data_object,key_primary_attr),
            getattr(data_object,key_secondary_attr),
            getattr(data_object,key_third_attr),
        )

    def set_key(self,name:str):
        self.key=getattr(self.object,name)
    
    
class RBThree:

    def __init__(self,root:Node,nil:Node):
        self.root=root
        self.nil=nil
    
def LEFT_ROTATE(T:RBThree,x:Node):
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

def RIGHT_ROTATE(T:RBThree,x:Node):
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


def RB_INSERT_FIXUP(T:RBThree,z:Node):
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
                    
def RB_INSERT(T:RBThree,z:Node):
    y=T.nil
    x=T.root
    while x!=T.nil:
        y=x   
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

def INORDER_THREE_WALK(T:RBThree,x:Node):
    if x!=T.nil:
        INORDER_THREE_WALK(T,x.left)
        print(x.key)
        INORDER_THREE_WALK(T,x.right)


def TREE_SEARCH(T:RBThree,x:Node,k:object):
    while x!=T.nil and k!=x.key:
        if k<x.key:
            x=x.left
        else:
            x=x.right
    return x

def THREE_MINIMUM(T:RBThree,x:Node):
    while x.left!=T.nil:
        x=x.left
    return x

def THREE_MAXIMUM(T:RBThree,x:Node):
    while x.right!=T.nil:
        x=x.right
    return x

def THREE_SUCCESSOR(T:RBThree,x:Node):
    if x.right!=T.nil:
        return THREE_MINIMUM(T,x.right)
    y=x.parent
    while y != T.nil and x==y.right:
        x=y
        y=y.parent
    return y

def THREE_PREDECESSOR(T:RBThree,x:Node):
    if x.left!=T.nil:
        return THREE_MAXIMUM(T,x.left)
    y=x.parent
    while y != T.nil and x==y.left:
        x=y
        y=y.parent
    return y



