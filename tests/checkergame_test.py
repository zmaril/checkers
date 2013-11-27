import unittest 
from checkergame import partitions2checkers,checkers2partitions,rtest

class TestCheckergame(unittest.TestCase):
    def test_partitions2checkers(self):
        #These tests are from the matrix in
        #"SOLVING SCHUBERT PROBLEMS"

        #Top row
        self.assertEqual(rtest(0,1,1,0,[1,0],2),([0,1],0))
        self.assertEqual(rtest(0,2,1,1,[2,99,1],3),([1,99,2],0))
        self.assertEqual(rtest(0,1,1,0,[1,99],2),([0,99],0))

        #Middle row
        self.assertEqual(rtest(0,1,2,0,[99,2,0],3),([0,99,2],0))
        self.assertEqual(rtest(0,2,2,1,[99,3,99,1],4),([99,3,99,1,1,99,99,3],1))
        self.assertEqual(rtest(0,1,2,0,[99,2,99],3),([99,2,99],0))

        #Bottom row
        self.assertEqual(rtest(0,1,1,0,[99,0],2),([0,99],0))
        self.assertEqual(rtest(0,2,1,1,[99,99,1],3),([99,99,1],0))
        self.assertEqual(rtest(0,1,1,0,[99,1],2),([99,1],0))

        #self.assertEqual(partitions2checkers(6,15,[1,1,1]),
#                         [9,10,11,13,14,15]) 
#Wrong but something weird is going on.
#
    
