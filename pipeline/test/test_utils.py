import unittest
import sys
import os
sys.path.append(os.path.abspath('../utils'))

from utils import *

class TestGraph(unittest.TestCase):

    def test_intersection(self):
        l1 = ["hello", "world", "hello", "again"]
        l2 = ["I", "use", "hello", "world", "a", "lot"]
        n = intersection(l1, l2)
        self.assertEqual(n,2)

    def test_remove_tags(self):
        text = "<p class = 'para'> Hi there</p>"
        text = remove_tags(text)
        self.assertEqual(text, " Hi there")

    def test_extract_tokens(self):
        text = "this function extract tokens from a sentence"
        tokens = extract_tokens(text)
        self.assertEqual(tokens, ["this", "function", "extract", "tokens", "from", "a", "sentence"])

    def test_clean_tokens(self):
        tokens = ["hello", "!", "this", "function", "extract", "tokens", "from", "a", "sentence", "."]
        tokens = clean_tokens(tokens)
        self.assertEqual(tokens, ["hello", "this", "function", "extract", "tokens", "from", "a", "sentence"])

    def test_remove_stop_words(self):

        tokens = ["I", "am", "working", "on", "machine", "learning", "challenge","for", "feedly"]
        tokens = remove_stop_words(tokens)
        self.assertEqual(tokens, ["I", "working", "machine", "learning", "challenge", "feedly"])