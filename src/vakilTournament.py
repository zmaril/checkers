#Test vakil's criterion for a schubert problem
from intersection import moveToFront, intersectionNum
from vakilTree import vakilTest
from vakilIterative import vakil_test
from checkergame import run


# this will be called several times, just run with different startPairs
# I may
def vakilTournament(checkerList, startPair):
  n = len(checkerList[0])  #all assumed correct
  k = n - checkerList[0].count(99)

  tournament = checkerList[:]

  tournament.remove(startPair[0])
  tournament.remove(startPair[1])

  first,second = startPair

  leaves, tree = run(first[:],second[:])


  intersections = []
  #check oracle for
  for leaf in leaves:
    if not askOracle(leaf,tournament,n,k):
      return False

    #get intersection number of list [leaf, tournament[0]...]
    tournCopy = tournament[:]
    tournCopy.insert(0,leaf)
    intersections.append(intersectionNum(tournCopy))

  return vakil_test(tree,intersections)
#  return vakilTest(tree,intersections)


def askOracle(leaf,theRest,n,k):
  checkers = leaf[:]
  checkerList = theRest[:]
  checkerList.insert(0,checkers)

  oracle = file('oracle/failures{0}_{1}.txt'.format(n,k),'r')
  while True:
    line = oracle.readline()
    if not line:
      break
    if eval(line) == checkerList:
      oracle.close()
      return False
  oracle.close()
  return True

#print vakilTournament([[99,99,99,3,99,5]]*3 + [[99,1,99,3,99,99]])
#print '-----------------------------------------'
#print vakilTournament([[99,99,99,3,99,5,6,7]]*7 + [[99,1,2,3,99,99,99,7]])
#print '-----------------------------------------'
#print vakilTournament([[99,99,2,99,4,5]]*9)
