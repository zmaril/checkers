from galoistest import *
from intersection import *
from vakilTournament import vakilTournament
from combinations import nextPair
from time import sleep


#TODO: rearrage k,n
#code mostly copied from go.py
def test_all(k,n):
  #initialize file
  outFile = open('oracle/failures{0}_{1}.txt'.format(n,k),'w')
  outFile.close()

  boxes = k*(n-k)
  shapes = get_all_parts(k,n)
  for m in range(3, boxes+1):  #3..boxes
    failures = []
    problem_type = [m-1] + (boxes-m)*[0]
    problem_type[-1] += 1
    shape_type = {}
    for i, item in enumerate(problem_type):
      shape_type[i+1] = len(shapes[i+1])*[0]
      shape_type[i+1][-1] = item
    while problem_type != []:
      print_prob, sch_prob = makeproblem(k, n, problem_type, shapes, shape_type)
      passed = vakil(sch_prob)
      if not passed:
        outFile = open('oracle/failures{0}_{1}.txt'.format(n,k),'a')
        outFile.write(str(sch_prob) + '\n')
        outFile.close()
      else:
        pass
        #print 'Testing ', sch_prob
      problem_type, shape_type = next_problem(k, n, problem_type, shapes, shape_type)
#    outFile.write("All problems of length {0} have been tested".format(m) + '\n')


def vakil(schProb):
  startPair = nextPair(schProb)
  while startPair != None:
    if vakilTournament(schProb,startPair):
      return True
    startPair = nextPair(schProb,startPair)
  return False



def test2planes(k):
  for n in range(4,k):
    test_all(2,n)


def test3planes(k):
  for n in range(3,k):
    test_all(3,n)
#go()
#test_all(3,5)

#test2planes(13)
print vakil ([[99, 99, 99, 99, 99, 99, 99, 99, 8, 99, 99, 11], [99, 99, 99, 99, 99, 99, 99, 7, 99, 99, 99, 11], [99, 99, 99, 99, 99, 5, 99, 99, 99, 99, 99, 11], [99, 99, 99, 99, 99, 5, 99, 99, 99, 99, 99, 11], [99, 99, 99, 99, 99, 5, 99, 99, 99, 99, 99, 11]])
