from galoistest import *
import pickle

def test_all_problems_G(k,n, db=0):
  boxes = k*(n-k)
  shapes = get_all_parts(k,n)
  #print("Master list of conditions: ", shapes)
  #m is the number of conditions
  for m in range(3, boxes+1):
    failures = []
    problem_type = [m-1] + (boxes-m)*[0]
    problem_type[-1] += 1
    shape_type = {}
    for i, item in enumerate(problem_type):
      shape_type[i+1] = len(shapes[i+1])*[0]
      shape_type[i+1][-1] = item
    while problem_type != []:
      print_prob, sch_prob = makeproblem(k, n, problem_type, shapes, shape_type)
      partlevel, treelevel, mults = get_entire_tree(sch_prob)
      if db == 0 and mults >= 4:
        print(vakiltest_nodb(partlevel, treelevel))
      if db == 1 and mults >= 4:
        fail = tournament(sch_prob, 1)
        if fail >= 1:
          print(print_prob, fail)
          failures.append(print_prob)
      problem_type, shape_type = next_problem(k, n, problem_type, shapes, shape_type)
    record_failures = open('failures_len_{0}.p'.format(m), 'wb')
    pickle.dump(failures, record_failures, -1)
    record_failures.close()
    print("All problems of length {0} have been tested".format(m))
  return "All problems on G({0},{1}) have been tested.".format(k,n)

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

