
RED='RED'
BLACK='RED'


class Node():
    def __init__(self,color:str,left:'Node',right:'Node',parent:'Node',key:object):
        self.color=color
        self.left=left
        self.right=right
        self.parent=parent
        self.key=key

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
                    



