from galoistest import makeproblem, get_all_parts, next_problem
from newMethod import GG2, Key
from multiprocessing import Pool
import random

def outer_gg(sch_prob):
  n = len(sch_prob[1])
  gg = GG2(Key(n,parts=sch_prob))
  if gg.alternating is False:
    return (sch_prob,gg)

def get_problems(k,n,m):
  boxes = k*(n-k)
  shapes = get_all_parts(k,n)
  problem_type = [m-1] + (boxes-m)*[0]
  problem_type[-1] += 1
  shape_type = {}

  for i, item in enumerate(problem_type):
    shape_type[i+1] = len(shapes[i+1])*[0]
    shape_type[i+1][-1] = item

  problems = []
  while problem_type !=[]:
    print_prob, sch_prob = makeproblem(k, n, problem_type, shapes, shape_type)
    yield sch_prob
    problem_type, shape_type = next_problem(k, n, problem_type, shapes, shape_type)

def test_all_problems_G(k,n, db=0):
  #pool = Pool()
  boxes = k*(n-k)
  failures = []
  #m is the number of conditions
  for m in range(3, boxes+1):
    failures.append(filter(None,map(outer_gg,get_problems(k,n,m))))
  return failures
