import unittest
from checkergame import rtest,run

class TestCheckergame(unittest.TestCase):
    def test_rtest(self):
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

    def test_run(self):
        self.assertEqual(run([99, 99, 99, 3, 99, 5], [99, 99, 99, 3, 99, 5]),([[99, 99, 99, 3, 4, 99], [99, 99, 2, 99, 99, 5]], {1: [2], 2: [0, 0]}))
        self.assertEqual(run([0, 99, 99, 99, 4, 5, 99, 7], [99, 99, 99, 3, 99, 5, 6, 7]),([[0, 99, 99, 99, 4, 5, 6, 99], [0, 99, 99, 3, 99, 5, 99, 7]], {1: [2], 2: [0, 0]}))
        self.assertEqual(run([0, 1, 99, 3, 99, 99], [99, 99, 2, 99, 4, 5]),([[0, 1, 2, 99, 99, 99]], {1: [0]}))
