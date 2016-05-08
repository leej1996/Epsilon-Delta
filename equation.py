

class Node:
    
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

class BinaryTree:

    def __init__(self, data):
        pass

class EquationTree:
    """ we base this off of djikstra's shunting algorithm """

    def __init__(self, equation):
        self.expressoin = equation.split()

class Equation:
    """ 
        a simple tree structure for an equation, allows for easy replacement of 
        variables with numbers
    """

    def __init__(self, equation):
        self.eq = EquationTree(equation)
        
