import unittest 
from intersection import intersectionNum

class TestIntersection(unittest.TestCase):

    def test_intersectionNum(self):
        self.assertEquals(intersectionNum([[99,99,99,3,99,5]]*3 + [[99,1,99,3,99,99]]),2)
        self.assertEquals(intersectionNum([[99,99,99,3,99,5,6,7]]*7 + [[99,1,2,3,99,99,99,7]]),20)
        self.assertEquals(intersectionNum([[99,99,2,99,4,5]]*9,(0,1)), 42)
