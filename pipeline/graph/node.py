class Node(object):
    """
    A class used to represent a node
    
    Attributes
    ----------
    id : int
        used to identify the node
    topic : str
        the topic of the article 
        represented by this node
    tokens: list of str
        list of the tokens of the article
    edges: list of int
        list of the nodes connected to this node
        
    Methods
    -------
    __str__()
        returns the id of the node with the edges 
    """
    def __init__(self, id, tokens):
        self.id = id
        self.tokens = list(tokens)
        self.edges = {}
        
    def __str__(self):  
        return "{" + str(self.id)+ ":" + str(list(self.edges.keys())) + "}\n"