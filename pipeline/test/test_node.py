import unittest
import sys
import os
sys.path.append(os.path.abspath('../graph'))
from node import Node

class TestNode(unittest.TestCase):

    def test_create(self):
        N = Node(1, ["hello", "world"])
        self.assertIsNotNone(N)
        self.assertEqual(N.id,1)
        self.assertEqual(N.tokens, ["hello", "world"])
        self.assertEqual(len(N.edges),0)
