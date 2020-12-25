from random import choices
import sys
import os

sys.path.append(os.path.abspath('../utils'))
from utils import intersection

class Graph(object):
    """
    A class used to represent a graph
    
    Attributes
    ----------
    nodes : dictionary
        used to store the nodes of the graph
    nodesNumber : int
        number of nodes in the graph

    Methods
    -------
    add_node(node)
        adds new node to the graph
    
    add_edge(node1, node2)
        adds edges between node1 and node1  
    
    add_edges(n)
        adds the edges between each two nodes
        if they share at least n tokens
    
    get_nodes()
        returns the list of nodes in the graph
    
    samples(n=10)
        print n random nodes with their edges
    """
    
    def __init__(self):
        """ initializes a graph object
        as an empty dictionary
        """
        self.nodes = {}
        self.nodesNumber = 0
        self.connectedComponents = None
        
    def add_node(self, node):
        """ Adds a new node to the graph
        if doesn't exist already
        
        Parameters
        ----------
        node : node
            the object node to add
        """
        if node in self.nodes:
            print("node ", node, " already exists in the graph")
        else:
            self.nodes[node.id] = node
            self.nodesNumber +=1
            
    def add_edge(self, node1, node2, weight):
        """ Adds an edge between node1 and node2
        if both exist in the graph
        
        Parameters
        ----------
        node1: node
        node2: node
        weight: int
            weight of the edge
        """
        if node1 not in self.nodes:
            print("node ", node1.id, " doesn't exist in the graph")
        
        elif node2 not in self.nodes:
            print("node ", node2.id, " doesn't exist in the graph")
        
        else:
            self.nodes[node1].edges[node2] = weight
            self.nodes[node2].edges[node1] = weight
    
    
    def add_edges(self, n):
        """Adds adges bewteen each two nodes of the graph
        if they share at least n tokens
        
        Parameters
        ----------
        n : int
            Number of tokens that each two nodes
            should share two have a link between them
        """
        nodes = list(self.nodes.keys())
        for i in range(len(nodes)):
            for j in range(i, len(nodes)):
                number_shared_tokens = intersection(self.nodes[i].tokens, self.nodes[j].tokens)
                if (i!=j) and (number_shared_tokens >= n):
                    self.add_edge(i, j, number_shared_tokens)
    
    def get_nodes(self):
        """ returns the list of the 
            nodes exist in the graph
        """
        return list(self.nodes.keys())
    
    def samples(self, n=10):
        """Prints n random nodes form the graph.
        If the argument n isn't passed in, the 
        default value
        
        Parameters
        ----------
        n : int, optional
            Number of samples to print (default is 10)
        """
        graph = "{\n"
        samples = choices(list(self.nodes.keys()), k = n)
        for i in samples:
            graph += str(self.nodes[i])+"\n"
        graph += "}"
        print(graph)
    
    def connected_components(self):
        """Finds the connected components in the graph
        
        Returns
        -------
        components: list of lists
            each sub-list represents a connected component
        
        """
        self.connectedComponents = []
        treated_nodes = {}
        for i in self.nodes:
            treated_nodes[i] = False
        
        for i in self.nodes:
            if not treated_nodes[i]:
                temp = []
                self.DFS(i, treated_nodes, temp)
                self.connectedComponents.append(temp)
                
        return self.connectedComponents
    
    def DFS(self, nodeId, treated_nodes, component):
        component.append(nodeId)
        treated_nodes[nodeId] = True

        for j in self.nodes[nodeId].edges:
            if not treated_nodes[j]:
                self.DFS(j, treated_nodes, component)
    
    def connected_components_number(self):
        """ Compute the number of components in the graph.
        """
        if not self.connectedComponents:
            self.connectedComponents = self.connected_components()
        return len(self.connectedComponents)
    
    def adjacency_matrix(self):
        """Compute the adjacenct matrix of the graph.
        """
        matrix = []
        for i in self.nodes:
            ligne = [0 for i in range(len(self.nodes))]
            for j in self.nodes[i].edges:
                ligne[j] = self.nodes[i].edges[j]
            matrix.append(ligne)
        return matrix #np.array([m for m in matrix])
            
    def __str__(self):
        graph = "{\n"
        for node in self.nodes:
            graph += str(self.nodes[node])+"\n"
        graph += "}"
        return graph

