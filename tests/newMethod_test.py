import unittest
from newMethod import GG,Key

class TestnewMethod(unittest.TestCase):
    def test_GG(self):
        r = GG(Key(8,[[99,99,2,3,99,99,6,7]]*4))
        self.assertEqual(r.solutions,6)
        self.assertEqual(r.alternating,False)
