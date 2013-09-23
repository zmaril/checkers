import unittest 
from combinations import allPairs, nextPair 

class TestCombinations(unittest.TestCase):

    def test_allPairs(self):
        self.assertEqual(allPairs([[99,1,99,3]]*4+[[0,99,2,99]]*2 + [[99,1,2,99]]),
                         [[[0, 99, 2, 99], [0, 99, 2, 99]],
                          [[0, 99, 2, 99], [99, 1, 2, 99]],
                          [[0, 99, 2, 99], [99, 1, 99, 3]],
                          [[99, 1, 2, 99], [99, 1, 99, 3]],
                          [[99, 1, 99, 3], [99, 1, 99, 3]]])
        self.assertEqual(allPairs([1,1,2,3,4]),[[1,1],[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]])
        self.assertEqual(allPairs("aaron"),[['a','a'],['a','n'],['a','o'],['a','r'],['n','o'],['n','r'],['o','r']])

    def test_nextPair(self):
        self.assertEqual(nextPair("aaron moore",['e','m']),['e','n'])
