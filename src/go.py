from galoistest import *
from newMethod import GG2, Key
from multiprocessing import Pool

def outer_gg(sch_prob):
  n = len(sch_prob[1])
  gg = GG2(Key(n,parts=sch_prob))
  if gg.alternating is False:
    return (sch_prob,gg)

def test_all_problems_G(k,n, db=0):
  pool = Pool()
  boxes = k*(n-k)
  shapes = get_all_parts(k,n)
  failures = []
  #m is the number of conditions
  for m in range(3, boxes+1):
    problem_type = [m-1] + (boxes-m)*[0]
    problem_type[-1] += 1
    shape_type = {}
    for i, item in enumerate(problem_type):
      shape_type[i+1] = len(shapes[i+1])*[0]
      shape_type[i+1][-1] = item
    
    problems = []
    while problem_type !=[]:
      print_prob, sch_prob = makeproblem(k, n, problem_type, shapes, shape_type)
      problems.append(sch_prob)
      problem_type, shape_type = next_problem(k, n, problem_type, shapes, shape_type)
      
    pool.map(outer_gg,problems)
  return failures

# Here is a sample script that walks through every possible schubert problem on
# G(4,8) with 8 conditions, for the purpose of seeing how the ordering works.
#k, n = 3,6
#shapes = get_all_parts(k, n); print("Master list of conditions: ", shapes)
#problem_type = [5,0,0,0,0,0,1]
#shape_type = {}
#for i, item in enumerate(problem_type):
#  shape_type[i+1] = len(shapes[i+1])*[0]
#  shape_type[i+1][-1] = item
#while problem_type != []:
#  print(problem_type, shape_type)
#  input()
#  problem_type, shape_type = next_problem(k, n, problem_type, shapes, shape_type)

#print(test_all_problems_G(3,5, 0))

