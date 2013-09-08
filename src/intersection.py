import checkergame

#
# Code to compute the intersection number of a schubert problem
# Aaron Moore 
#
# ****************************************************************************
# 
# moveToFront
# input: list and a tuple containing two ints < len(List) and first != second
# output: list
#
# Switches List[0] <-> List[first], and List[1] <-> List[second]
#*****************************************************************************
def moveToFront(List,(first,second)):
  if first >= len(List) or second >= len(List) or first == second:
    return List

  array = List[:]
  #possibly change to just push them in front instead of switching
  array[0], array[first] = array[first], array[0]
  array[1], array[second] = array[second], array[1]
  return array

# ****************************************************************************
#
# removeDeadLeaves
# input: list of checker positions all lists of same length
# output: list of checker positions without all 99's
#
# Careful! modifies leaves
# ****************************************************************************

def removeDeadLeaves(leaves):
  if leaves == []:
    return []

  boardSize = len(leaves[0])
  #give name to cryptic none condiiton
  null = boardSize * [99]

  #remove all null conditions
  for i in range(leaves.count(null)):
    leaves.remove(null)

  return leaves

#TODO: 
#      benchmarks
# ****************************************************************************
#
# intersectionNum
# input: list of checker positions, tuple of which go first, boolean
# output: int
#
# Computes the intersection number of a Schubert problem
# ****************************************************************************

def intersectionNum(conditions, startPair= (0,1), debug=False):
  tournament = moveToFront(conditions,startPair)

  # run first two against each other
  first = tournament.pop(0)
  second = tournament.pop(0)
  currentLeaves, tree = checkergame.run(first[:], second[:])
  removeDeadLeaves(currentLeaves)
  
  if debug == True:
    print 'running first->', first, ' against second->',second
    print 'results'
    print 'currentLeaves =', currentLeaves
 
  # Fact: there is only one path to all leaves at first level
  mults = [1]*len(currentLeaves)

  it = 0  # simply keeps track iteration level
  # for each condition in tournament
  for cond in tournament: 
    it += 1
    newLeaves = []
    newMults = []
    # for each current leaf to be run against new condition
    j = 0
    if debug:
      print '------------------------------------'
      print 'current iteration -> ', it+2
    for leaf in currentLeaves:
      if debug:
        print 'running leaf-> ', leaf, ' against cond-> ',cond

      # run the two against each each other
      newResults, tree = checkergame.run(leaf,cond)
      if debug:
        print tree

      newLeaves.extend(newResults)
      removeDeadLeaves(newResults)
      removeDeadLeaves(newLeaves)
      
      #multiplicity propagates to leaves
      newMults.extend(len(newResults)*[mults[j]])
      j += 1

    if debug:
      print 'newLeaves->', newLeaves
      print 'newMults->', newMults

    #make the new list of leaves
    currentLeaves = []
    mults = []
    for i in range(len(newLeaves)):
      if newLeaves[i] not in currentLeaves:
        currentLeaves.append(newLeaves[i])
        mults.append(newMults[i])
      else:
        j = currentLeaves.index(newLeaves[i])
        mults[j] += newMults[i]
    
    if debug:
      print 'currentLeaves->', currentLeaves
      print 'mults->', mults

  if len(mults) == 1:
    return mults[0]
  else:
    return 0


#print intersectionNum([[99,99,99,3,99,5]]*3 + [[99,1,99,3,99,99]]) # output: 2
#print intersectionNum([[99,99,99,3,99,5,6,7]]*7 + [[99,1,2,3,99,99,99,7]])  # output: 20
#print intersectionNum([[99,99,2,99,4,5]]*9,(0,1),True) # output: program trace, result: 42
