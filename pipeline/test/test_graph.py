import unittest 
import sys
import os
sys.path.append(os.path.abspath('../graph'))
sys.path.append(os.path.abspath('../utils'))
from graph import Graph
from utils import *
from node import Node


class TestGraph(unittest.TestCase):

    def test_create(self):
        G = Graph()
        self.assertIsNotNone(G)
        self.assertEqual(len(G.nodes),0)
        self.assertEqual(G.nodesNumber,0)
        self.assertIsNone(G.connectedComponents)
    
    def test_add_node(self):
        G = Graph()
        G.add_node(Node(1, ["hello", "world"]))
        self.assertEqual(len(G.nodes),1)
        self.assertEqual(G.nodesNumber, 1)

    def test_add_edge(self):
        G = Graph()
        G.add_node(Node(0, ["hello", "world"]))
        G.add_node(Node(1, ["hello", "Again"]))
        G.add_edges(1)
        self.assertIn(1, G.nodes[0].edges)
        self.assertIn(0, G.nodes[1].edges)

    def test_get_nodes(self):
        G = Graph()
        G.add_node(Node(0, ["hello", "world"]))
        G.add_node(Node(1, ["hello", "Again"]))
        self.assertEqual(G.get_nodes(), [0, 1])

    def test_connected_components(self):
        G = Graph()
        G.add_node(Node(0, ["hello", "world"]))
        G.add_node(Node(1, ["hello", "world", "again"]))
        G.add_node(Node(2, ["hello", "world", "for", "the", "third", "time" ]))
        G.add_node(Node(3, ["This", "code", "is", "for", "testing", "graph", "class"]))
        G.add_node(Node(4, ["graph", "class", "contains", "many", "methods"]))
        G.add_edges(2)
        connected_components = G.connected_components()
        self.assertEqual(connected_components, [[0,1,2], [3,4]])
        self.assertEqual(G.connected_components_number(), 2)
    
    def test_adjacency_matrix(self):
        G = Graph()
        G.add_node(Node(0, ["hello", "world"]))
        G.add_node(Node(1, ["hello", "world", "again"]))
        G.add_node(Node(2, ["hello", "world", "for", "the", "third", "time" ]))
        G.add_node(Node(3, ["This", "code", "is", "for", "testing", "graph", "class"]))
        G.add_node(Node(4, ["graph", "class","code", "contains", "many", "methods"]))
        G.add_edges(2)
        adjacency_matrix = G.adjacency_matrix()
        self.assertEqual(adjacency_matrix, [[0,2,2,0,0],\
                                            [2,0,2,0,0],\
                                            [2,2,0,0,0],\
                                            [0,0,0,0,3],\
                                            [0,0,0,3,0]])