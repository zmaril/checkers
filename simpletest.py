import unittest
from newMethod import GG,Key

class TestnewMethod(unittest.TestCase):
    def test_GG(self):
        r = GG(Key(8,[[99, 99, 99, 3, 99, 5, 6, 7], [99, 99, 99, 3, 99, 5, 6, 7], [99, 99, 99, 3, 99, 5, 6, 7], [99, 99, 99, 3, 99, 5, 6, 7], [99, 99, 99, 3, 99, 5, 6, 7], [99, 99, 99, 3, 99, 5, 6, 7], [99, 1, 99, 3, 99, 99, 6, 7], [99, 1, 99, 3, 99, 99, 6, 7]]))
        self.assertEqual(r.solutions,80)
        self.assertTrue(r.alternating)
