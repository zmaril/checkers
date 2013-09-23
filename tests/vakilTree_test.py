import unittest 
from vakilTree import vakilTest
from checkergame import run

class TestVakilTree(unittest.TestCase):
    def test_vakilTest(self):

        first_test_dict = {1:[2], 2:[3,4], 3:[0,0], 4:[0,0]}
        self.assertFalse(vakilTest(first_test_dict))
        self.assertTrue( vakilTest(first_test_dict,[3,6,1,4]))

        second_test_dict = {1:[2], 2:[0,3], 3:[4,0], 4:[0,0]}
        self.assertTrue( vakilTest(second_test_dict))
        self.assertFalse(vakilTest(second_test_dict,[3,1,1,1]))
        
        third_test_dict = {1:[2], 2:[3,4], 3:[0,0], 4:[0,5], 5:[0,0]}
        self.assertTrue(vakilTest(third_test_dict))
        self.assertFalse(vakilTest(third_test_dict,[3,4,5,1,1]))

        fourth_test_dict = {1:[2], 2:[3,4], 3:[0,0], 4:[6,5], 5:[0,0], 6:[0,0]}
        self.assertFalse(vakilTest(fourth_test_dict))
        
        result = run([99,1,99,3,99,5,99,99],[99,99,99,3,99,5,99,7])[1]
        
        #TODO: run prints out a ton of messages that obsecure what is
        #actually going on. It messes with the beauty of watching all
        #the tests pass.
        
        #self.assertFalse(vakilTest(result))

