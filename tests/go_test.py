from go import test_all_problems_G, outer_gg
import unittest

case1 = [[99, 99, 99, 3, 99, 5, 6, 7], [99, 99, 99, 3, 99, 5, 6, 7], [99, 99, 2, 3, 99, 99, 6, 7], [99, 1, 99, 3, 99, 99, 6, 7], [99, 1, 99, 3, 99, 99, 6, 7]]

case2 = [[99, 99, 2, 99, 4, 99, 6, 7], [99, 99, 2, 99, 4, 99, 6, 7], [99, 1, 99, 99, 99, 5, 6, 7], [99, 1, 99, 99, 99, 5, 6, 7], [99, 99, 2, 3, 99, 99, 6, 7]]

case3 = [[99, 99, 99, 3, 99, 5, 6, 7], [99, 99, 99, 3, 99, 5, 6, 7], [99, 99, 99, 3, 99, 5, 6, 7], [99, 99, 99, 3, 99, 5, 6, 7], [99, 99, 99, 3, 99, 5, 6, 7], [99, 99, 99, 3, 99, 5, 6, 7], [99, 1, 99, 3, 99, 99, 6, 7], [99, 1, 99, 3, 99, 99, 6, 7]]

class TestGo(unittest.TestCase):
    def test_outer_gg(self):
        r = outer_gg(case1)[1]
        self.assertEqual(r.solutions,8)
        self.assertTrue(r.alternating)

        r = outer_gg(case2)
        self.assertEqual(r.solutions,8)
        self.assertTrue(r.alternating)

        r = outer_gg(case3)
        self.assertEqual(r.solutions,80)
        self.assertTrue(r.alternating)

#     def test_all_problems_G(self):        
#         self.assertEqual(len(test_all_problems_G(2,2)),0)
#         self.assertEqual(len(test_all_problems_G(2,3)),0)
#         self.assertEqual(len(test_all_problems_G(2,4)),0)
#         self.assertEqual(len(test_all_problems_G(2,5)),0)
#         self.assertEqual(len(test_all_problems_G(2,6)),0)

#         self.assertEqual(len(test_all_problems_G(3,3)),0)
#         self.assertEqual(len(test_all_problems_G(3,4)),0)
#         self.assertEqual(len(test_all_problems_G(3,5)),0)
#         self.assertEqual(len(test_all_problems_G(3,6)),2)
#         #TODO Check 3,7 3,8
#         self.assertEqual(len(test_all_problems_G(3,7)),8) #Is that right?

#         self.assertEqual(len(test_all_problems_G(4,4)),0)
#         self.assertEqual(len(test_all_problems_G(4,5)),0)
#         self.assertEqual(len(test_all_problems_G(4,6)),0)
#         self.assertEqual(len(test_all_problems_G(4,7)),8)
#         self.assertEqual(len(test_all_problems_G(4,8)),83) #TODO

        

# #        self.assertEqual(len(test_all_problems_G(4,8)),2)
# #        self.assertEqual(len(test_all_problems_G(4,9)),233)




