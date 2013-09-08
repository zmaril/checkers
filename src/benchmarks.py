from galoistest import *
from intersection import *


#code mostly copied from go.py
def test_all_intersection(k,n,fileName=None):
  outFile = None
  if fileName:
    outFile = open(fileName,'w')
    outFile.write('All problems for G('+str(k)+','+str(n)+')\n\n')
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
      inter = intersectionNum(sch_prob)
      
      if(outFile):
        outFile.write(str(sch_prob) + ' = ' + str(inter) + '\n')
      else:
        #turns checkers into more readable partitions
        #comment out to print checkerpositions
        sch_prob = map(checkers2partitions,sch_prob)
        print sch_prob, ' = ', inter
      problem_type, shape_type = next_problem(k, n, problem_type, shapes, shape_type)
    if(outFile):
      outFile.write("All problems of length {0} have been tested".format(m) + '\n')
    else:
      print("All problems of length {0} have been tested".format(m))

  if(outFile):
    outFile.close


def run_benchmarks():
  for n in range(4,8):
    for k in range(2,n-1):
      fileName = 'G_' + str(k) + '_' + str(n) + '.txt'
      test_all_intersection(k,n,fileName)

test_all_intersection(3,5)
