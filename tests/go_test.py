from go import test_all_problems_G
import unittest

class TestGo(unittest.TestCase):
    def test_all_problems_G(self):
        self.assertEqual(len(test_all_problems_G(2,2)),0)
        self.assertEqual(len(test_all_problems_G(2,3)),0)
        self.assertEqual(len(test_all_problems_G(2,4)),0)
        self.assertEqual(len(test_all_problems_G(2,5)),0)
        self.assertEqual(len(test_all_problems_G(2,6)),0)

        self.assertEqual(len(test_all_problems_G(3,3)),0)
        self.assertEqual(len(test_all_problems_G(3,4)),0)
        self.assertEqual(len(test_all_problems_G(3,5)),0)
        self.assertEqual(len(test_all_problems_G(3,6)),2)
        #TODO Check 3,7 3,8
        self.assertEqual(len(test_all_problems_G(3,7)),8) #Is that right?

        self.assertEqual(len(test_all_problems_G(4,4)),0)
        self.assertEqual(len(test_all_problems_G(4,5)),0)
        self.assertEqual(len(test_all_problems_G(4,6)),0)
        self.assertEqual(len(test_all_problems_G(4,7)),8)
        self.assertEqual(len(test_all_problems_G(4,8)),83) #TODO

        

#        self.assertEqual(len(test_all_problems_G(4,8)),2)
#        self.assertEqual(len(test_all_problems_G(4,9)),233)




