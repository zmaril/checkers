from checkergame import *
import pickle

# tournament.py
#
# Christopher Brooks
#

################################################################################
# get_entire_tree
################################################################################
#
# Running Vakil's checker game on the list of conditions 'tournin' results in a
# large tree.
#
#  tourn:         a list of schubert conditions (checker positions) in G(k,n)
#  q:             how high we are in the tree (starts at 0)
#  treelevel[q]:  a list of all the subtrees (in order) at level q
#  partlevel[q]:  a list of all the paritions (in order) at level q
#  mults:         a list of multiplicities of the things the current partlevel
#
def get_entire_tree(tournin, startpair=(0,1), verb=0):
  tourn = tournin[:]
  tourn[0], tourn[startpair[0]] = tourn[startpair[0]], tourn[0]
  tourn[1], tourn[startpair[1]] = tourn[startpair[1]], tourn[1]
  tourn_copy = tourn #copies the input so I can use it in newvakiltest
  treelevel=[[]]; q=0; n=len(tourn[0])
  #Start the multiplication, initialize the list of multiplicities
  tourn[0], treebase = run(tourn[0][:], tourn.pop(1))

  mults=len(tourn[0])*[1]

  #Remove dead leaves
  for i in range(tourn[0].count(n*[99])):
    mults.pop(tourn[0].index(n*[99]))
    tourn[0].remove(n*[99])
  treelevel[0].append(treebase)
  partlevel=[tourn[0][:]]
  x=tourn.pop(0)
  while len(tourn)>0:
    if verb==1:
      print(q)
      print 'treelevel[q]-> ', treelevel[q]
      print 'partlevel[q]->, ', partlevel[q]
      print 'mults-> ', mults
      print('-----------------')
    q += 1; treelevel.append([])
    y=tourn.pop(0)
    #This loop multiplies the fixed variety y against the union of varieties
    #in x (i.e. the leaves from the previous step)
    for i in range(len(x)):
      x[0], trees = run(x[0][:], y[:])
      localcount=len(x[0])*[1]
      #Record the tree from every checker game
      treelevel[q].append(trees)
      #Queue the next variety for multiplying, since we always run against x[0]
      x.extend(x.pop(0))
      mults.extend([mults[0]*j for j in localcount])
      mults.pop(0)
    for i in range(x.count(n*[99])):
      mults.pop(x.index(n*[99]))
      x.remove(n*[99])

    #Record the indices of duplicate leaves, and replace duplicates with a zero.
    endpoint = len(x)
    indices={}
    for i in range(endpoint):
      if x[i] == 0:
        continue
      for j in range(i+1, endpoint):
        if x[i] == x[j]:
          x[j]=0
          mults[i] += mults[j]
          mults[j] = 0
          indices[j] = i
    partlevel.append(x[:])
    #Now wherever there was a duplicate, we place the index of the original
    for i in range(len(partlevel[q])):
      if partlevel[q][i]==0:
        partlevel[q][i]=indices[i]
    for i in range(x.count(0)):
      x.remove(0)
      mults.remove(0)

  if verb==1:
    print(q)
    print(treelevel[q])
    print(partlevel[q])
    print('-----------------')
  if mults==[]:
    mults=0
  #At the end there is only one thing in multiplicities
  else:
    mults=mults[0]
  return partlevel, treelevel, mults

#p,t,m = get_entire_tree([[99, 99, 2, 99, 4, 5], [99, 1, 2, 99, 99, 5], [99, 1, 2, 99, 99, 5]], [0,2], 1)


################################################################################
# schind
################################################################################
#
# Given a tree and 'm' a list of multiplicities for each leaf of the tree, we
# go to every node and we find out how may leaves are above that node. Also,
# while doing this, we check for the number of leaves above and to the left and
# compare it to the number of leaves above and to the right to see if Vakil's
# criterion holds at each node. Output is a single number (which is just the sum
# of 'm') and the degree of failure. A failure of 2 indictes that Vakil's crit.
# failed somewhere in the middle of the tree, while a failure of 3 indicates
# that it failed at the base of the tree. I don't think this really makes a
# difference, so for now just consider these failures as both > 2.
#
def schind(tree,m):
  if tree=={1:[0]}:
    return m[0], 0

  #We start to the left of node no. 1; k is the current working node
  k=tree[1][0]
  fail=0
  while 1:
    #print(tree); print(k); print('')
    #Case: k points directly to its multiplicities (an integer)
    if type(tree[k])==type(int()):
      #Find the first node 'i' pointing to 'k'
      for i in range(2, len(m)+1):
        if type(tree[i])==type(list()) and k in tree[i]:
          break#out of 'for' loop
      #If there is nothing pointing to 'k', we are done
      if k==i==len(m):
        break#out of 'while' loop
      #Otherwise, go to that node
      else:
        k = i
        continue

    #Case: node k has no nodes above it, so just add corr. multiplicities
    elif tree[k]==[0,0]:
      tree[k] = m[k-2] + m[k-1]
      if m[k-2]==m[k-1] and m[k-2]!=1:
        fail=2
        #print(m[k-2], m[k-1])
        if k==tree[1][0]: fail=3

    #Case: node k has a node to the right only
    elif tree[k][0]==0:
      #Try to get a number from the right
      try: tree[k] = m[k-2] + tree[tree[k][1]]
      #If this is impossible, go to that node and try to collapse it further
      except TypeError:
        k = tree[k][1]; continue
      if tree[k]==2*m[k-2] and m[k-2]!=1:
        fail=2
        #print(m[k-2], tree[k])
        if k==tree[1][0]: fail=3

    #Case: node k has a node to the left only. Same as above case
    elif tree[k][1]==0:
      try: tree[k] = tree[tree[k][0]] + m[k-1]
      except TypeError:
        k = tree[k][0]; continue
      if tree[k]==2*m[k-1] and m[k-1]!=1:
        fail=2
        #print(m[k-1], tree[k])
        if k==tree[1][0]: fail=3

    #Case: node k has nodes on both sides and tree[k][0] is fully collapsed.
    elif type(tree[tree[k][0]])==type(int()):
      b = tree[tree[k][0]]
      #Same as above cases; try to add them together
      try: tree[k] = tree[tree[k][0]] + tree[tree[k][1]]
      except TypeError:
        #This is not an arbitrary choice, see comment (*) below
        k = tree[k][1]; continue
      if tree[k]==2*b and tree[k]!=2:
        fail=2
        #print(b, tree[k])
        if k==tree[1][0]: fail=3
    #Last case (else): k has nodes on both sides but tree[k][0] is not an int.
    #Note that if we test tree[k][0] above (*) and here k=tree[k][1], then this
    #algorithm doesn't terminate. This is an artifact of the choice of the
    #ordering of nodes we adopted in checkergame.py
    else:
      k = tree[k][0]; continue
  return(tree[tree[1][0]], fail)

################################################################################
# vakiltest_nodb
################################################################################
#
# This routine tests vakil's criterion. A return of 2 means a strong fail, 1
# means a weak fail, and 0 is a pass. q is the total number of levels (as in
# the checkertourn routine)
#
#  q:        The height of the tree (as in checkertourn)
#  part[i]:  A list of partitions at level i of the tree
#  tree[i]:  A list of subtrees at level i of the tree
#
def vakiltest_nodb(in_part, in_tree):
  q = len(in_part)-1
  part = in_part[:]
  tree = in_tree[:]
  mults = len(part[q])*[1]
  probfail = 0
  while q >= 0:
    for i in range(len(part[q])): #Replace partitions with their multiplicities
      if type(part[q][i]) == type(list()):
        part[q][i] = mults.pop(0)
      else:
        #If part[q][i] is an int, it is a duplicate, so go to the original.
        part[q][i] = part[q][part[q][i]]
    #In the previous iteration of the loop we replaced part[q] with the mults
    #above it, so part[q] is the new mults.
    mults = part[q]
    for i in range(len(tree[q])):
      if tree[q][i] == {}:
        mults.append(0)
        continue
      z = len(tree[q][i])
      newmults, treefail = (schind(tree[q][i], mults[0:z]))
      #print(treefail, "   q=", q)
      mults[0:z] = []
      mults.append(newmults)
      if treefail>probfail:
        probfail = treefail
      if probfail == 2 and q > 0:
        probfail = 1
    q -= 1
  return probfail

def in_fail_db(test_prob_in, known_failures):
  test_prob = []
  for i in test_prob_in:
    test_prob.append(checkers2partitions(i[:]))
  #test_prob needs to be put in the correct order
  test_prob.sort(key = lambda b: tuple(b[i] for i in range(len(b)-1, -1, -1)))
  test_prob.sort(key = lambda b: len(b))
  test_prob.sort(key = lambda b: sum([b[i]*(i+1) for i in range(len(b))]))
  if test_prob in known_failures:
    return 1
  else:
    return 0

################################################################################
# vakiltest_db
################################################################################
#
# This is a variant of the vakiltest algorithm which uses a database (or some
# other way of recalling problems already solved) to change the number of
# permutations from n factorial to n choose 2.
#
# We take the first row of partitions (as output by get_entire_tree) and we
# match each entry with tournin (omitting the two that produced the first row)
# to look at the problems with m-1 conditions. Then we search for these problems
# in a list of previously known failures. If there are no failures of length m-1
# then we know the only possible failure would be at the base of the tree (q=0
# in get_entire_tree notation).
#
def vakiltest_db(row1_partitions, base_tree, tournin, start):
  i = start[0]; j = start[1]
  m = len(tournin)
  #i and j were the indices which made row 1, so remove those entries.
  tournin.pop(j); tournin.pop(i)
  row_fail = 0
  #We need the multiplicities of each leaf on row 1
  row1_mults = []

  #Acquire a list of all known failures with m-1 conditions.
################################################################################
################################################################################

  try:
    known_failures_pkl = open('failures_len_{0}.p'.format(m-1), 'rb')
    known_failures = pickle.load(known_failures_pkl)
  except IOError:
    print("No such file 'failures_len_{0}'".format(m-1))
    known_failures = []
  for j in row1_partitions:
    #Make a schubert problem with m-1 conditions.
    try:
      test_prob = [j[:]] + tournin
      row1_mults.append(get_entire_tree(test_prob[:])[2])
    #If j is not a list, then it points to its duplicate, so go there.
    except TypeError: 
      row1_mults.append(row1_mults[j])
    if in_fail_db(test_prob, known_failures):
      row_fail = 1; print("Row failure.")
  #Finally, we need to check for failure at the base.
  base_fail = schind(base_tree, row1_mults)[1]
  if base_fail > 0: print("Failure at the base. ", base_fail)
  #Failure at the base is stronger since it doesn't come from a smaller problem
  fail = max(base_fail, row_fail)
  return fail

################################################################################
# tournament
################################################################################
#
# return of 1 indicates failure; 0 means passing
#
def tournament(tournin, test_vakil=0):
  fail = 3#Guilty until proven innocent
  m = len(tournin)
  partitions, trees, numsolns = get_entire_tree(tournin[:])
  if test_vakil==0:
    return numsolns
  start=[0,0,0]
  next=[0,0]
  while 1:
    if next[1] < m-1:
      next[1] += 1
    elif next[1] - next[0] > 1:
      next[0] += 1
      next[1] = next[0]+1
    else:
      break
    test1 = tournin[next[0]]==tournin[start[0]]
    test2 = tournin[next[1]]==tournin[start[1]]
    if test1 and test2 and len(start)==2:
      start = next[:]
      continue
    start = next[:]
    partitions, trees, numsolns = get_entire_tree(tournin[:], start[:])
    fail=min(vakiltest_db(partitions[0],trees[0][0],tournin[:],start[:]),fail)
    if fail == 0:
      return 0
  return 1
