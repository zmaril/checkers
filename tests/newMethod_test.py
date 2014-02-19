import unittest
from newMethod import GG,Key

class TestnewMethod(unittest.TestCase):
    def test_GG(self):
        r = GG(Key(8,[[99,99,2,3,99,99,6,7]]*4))
        self.assertEqual(r.solutions,6)
        self.assertFalse(r.alternating)

        r = GG(Key(6,[[99,99,2,99,4,5]]*3+[[99,1,99,3,99,5]]*2))
        self.assertEqual(r.solutions,6)
        self.assertTrue(r.alternating)

        r = GG(Key(8,[[99, 99, 99, 3, 99, 5, 6, 7], [99, 99, 99, 3, 99, 5, 6, 7], [99, 99, 99, 3, 99, 5, 6, 7], [99, 99, 99, 3, 99, 5, 6, 7], [99, 99, 99, 3, 99, 5, 6, 7], [99, 99, 99, 3, 99, 5, 6, 7], [99, 1, 99, 3, 99, 99, 6, 7], [99, 1, 99, 3, 99, 99, 6, 7]]))
        self.assertEqual(r.solutions,80)
        self.assertTrue(r.alternating)

        
