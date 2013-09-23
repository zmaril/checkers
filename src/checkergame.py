# checkergame.py
#
# Christopher Brooks
# June 27, 2012 - edits:Aaron Moore
# 
################################################################################
# This code contains functions to deal with Vakil's checker game,
# which is a way of encoding the geometric Littlewood-Richardson rule.
#
# To start, use the function "run".
#
# input: red checker initial positions, dimension of the ambient space
# output: list of red checker positions


################################################################################
# partitions2checkers, checkers2partitions
################################################################################
#
# Converts a partition in multiplicity form to a checker input and
# vice versa
#
# k, n : size of the grassmannian
# part : partition in multiplicity form
# checkers : a list of checker positions (see checkergame.py)
#
def partitions2checkers(k, n, part):
  #First we change to a standard form, i.e. if 'part' is [2,3,4] then
  #'standard' will be [3,3,3,3,2,2,2,1,1]
  standard = []
  for i in range(len(part)-1,-1,-1):
    standard.extend(part[i]*[i+1])
  #Now we walk the edge of the partition, appending 'checkers'
  #wherever there is a downstep
  checkers = []
  checkers.append(n-k-standard[0])
  m = len(standard)
  for i in range(1, m):
    checkers.append(standard[i-1] - standard[i] + 1 + checkers[-1])
  #end_list accounts for downsteps on empty rows
  end_list = [n-i for i in range(k-m,0,-1)]
  checkers.extend(end_list)
  out_checkers = n*[99]
  #print out_checkers
  for i in checkers:
    out_checkers[i] = i
    #print out_checkers, i
  return out_checkers


def checkers2partitions(checkers):
  out_std = []
  for i in range(len(checkers)):
    if checkers[i] != 99:
      out_std.append(checkers[i+1:].count(99))
  out = max(out_std)*[0]
  for i in out_std:
    if out[i-1] == 0:
      out[i-1] = out_std.count(i)
  return out

################################################################################
# rtest
################################################################################
#
# Moves the red checkers. This calculates one turn for the "game"
# routine below.
#
# input:
#       x1, y1 - Coordinates of the ascending black checker
#       x2, y2 - Coordinates of the descending black checker
#       R - List of red checker positions
#       n - Dimension of the board
#
#	output:
#       R - Updated list of red checker positions
#       sp - "1" if a split occured, "0" otherwise
#
def rtest(x1, y1, x2, y2, R, n):
  greek=2; roman=2; sp=0
  #Find the critical row, "cr".
  for col in range(n-1, x2-1, -1):
    if R[col] == y2:
      cr = col
      if col == x2: 
        greek = 0
      else:
        greek = 1
  #Find the critical diagonal, "cd".
  for col in range(x2-1, -1, -1):
    if x2-col+R[col] == n:
      cd = col
      if (y1, x1) == (R[col], col):
        roman = 0
      else:
        roman = 1
  if roman == 0:
    R[x1] = R[x1]-1
    if greek == 0:
      R[x2] += 1
    if greek == 1:
      R[cr] += 1
  if roman == 1:
    if greek == 0:
      R[cr] = R[cd]
      R[cd] = 99
      R[x1] = y2
    if greek == 1:
      block=0
      for blockpos in range(cr-1, cd, -1):
        if R[cr] < R[blockpos] < R[cd]:
          block=1
      if block!=1:
        rts = R[0:n]
        #Switch the rows of the red checkers in the critical diagonal
        #and row, then move the left checker over to the column of the
        #ascending black checker. Then we save the state of the red
        #checkers so 'game' can come back to this branch later and go
        #the other way. (See the example)
        rts[cr] = rts[cd]
        rts[cd] = 99
        rts[x1] = y2
        for i in range(0,n):
          R.insert(n, rts[n-1-i])
          sp = 1#Flag that indicates that split occured
  if roman == 2 and greek == 0:
    R[x1] = R[cr]
    R[cr] = 99
  return R, sp


################################
# game
################################
#
#Moves black checkers using Vakils geometric Littlewood-Richardson
#rule
# 
# input:
#       B - List of black checker positions
#       R - List of red checker positions
#       n - dimension of the board
#
# output:
#       B - Updated list of black checker positions
#       R - Updated list of red checker positions
#

def game(B, R, n):
  splitcount=0
  save=[]
  #Determine the columns of the descending and ascending checkers.
  desc_col=1+B.index(n-1)
  asc_col=B.index(1+B[desc_col])
  #The column of the right black checker to be sorted goes from
  #desc_col to the end of the board.
  for x2 in range(desc_col, n):
    #The next for-loop needs to start at 0 except at the beginning.
    if x2==desc_col+1:
      asc_col=0
    #The column of the left black checker to be sorted goes from the
    #beginning of the board to "x2".
    for x1 in range(asc_col, x2):
      #Determine the rows of the next pair of black checkers to be sorted.
      y1 = n - x2 + x1
      y2 = y1 - 1
      #Red and black checkers are moved. "copy" is switched to 1 when
      #a split occurs in "rtest"
      R, copy = rtest(x1, y1, x2, y2, R, n)
      B[x1] = B[x1]-1
      B[x2] = B[x2]+1
      if copy == 1:
        #Records the state of the black checkers. Queues it
        for i in range(0,n):
          B.insert(n, B[n-1-i])
        splitcount = splitcount + 1
  return B, R, splitcount


# intended to run exactly like game, except it stops both games on a
# split whereas, game runs the 'leftmost' game through to the end
def gamePreemptive(B,R,n):
  splitcount = 0;
  save=[]
  #Determine the columns of the descending and ascending checkers.
  desc_col=1+B.index(n-1)
  asc_col=B.index(1+B[desc_col])
  #The column of the right black checker to be sorted goes from
  #desc_col to the end of the board.
  for x2 in range(desc_col, n):
    #The next for-loop needs to start at 0 except at the beginning.
    if x2==desc_col+1:
      asc_col=0
    #The column of the left black checker to be sorted goes from the
    #beginning of the board to "x2".
    for x1 in range(asc_col, x2):
      #Determine the rows of the next pair of black checkers to be
      #sorted.
      y1 = n - x2 + x1
      y2 = y1 - 1
      #Red and black checkers are moved. "copy" is switched to 1 when
      #a split occurs in "rtest"
      R, copy = rtest(x1, y1, x2, y2, R, n)
      B[x1] = B[x1]-1
      B[x2] = B[x2]+1
      if copy == 1:
        #Records the state of the black checkers. Queues it
        for i in range(0,n):
          B.insert(n, B[n-1-i])
        splitcount = splitcount + 1
        return B,R,splitcount #return both options rather than
                              #continuing the left path
  return B, R, splitcount


#Example of 'game' (starting from the middle of a checker game)
#a=[3,2,1,0]; b=[99,3,99,1],
#print(a,b,4),
#print(game(a, b, 4))

################################################################################
# maketree
#############################################################################
# The binary trees used in the tournament routines are stored in
# python as dictionaries (another term for a hash table). Every node
# in the tree gets a number which corresponds to the index of the leaf
# in the output of "run". The python dictionary is a mapping whose
# input is the node number and the output is the pair of nodes
# directly above it. The "maketree" routine constructs this dictionary
# using the following method.

# The "run" algorithm prefers a certain direction in the tree. A node,
# say m (>1) corresponds with a leaf if you start at node m, go right
# once, then go left until the leaf. The 1st node, or root,
# corresponds to the 1st leaf; i.e. by starting at node 1 and only
# taking left branches, you will reach the 1st zero.

# To understand the algorithm, one needs to understand how the input
# determines the tree structure. As an example, take
# [1,1,2,3,3,3]. This indicates that as you travel from the first node
# to the first leaf (as always, in the default direction) two nodes
# are encountered, hence [1,1]. These are the splits from the checker
# game. Then you backtrack to the nearest node and call it 2. As you
# head to the second leaf from 2, you encounter one split, as
# indicated by [2].  Last, you backtrack to the nearest node and call
# it 3. Then [3,3,3] indicates that 3 splits are encountered. Any
# unfinished nodes go directly to leaves, and are numbered in order as
# you backtrack through the tree.

# For the "maketree" algorithm, consider [1,1,1,2,3,3,4,7,7] as
# input. It helps to draw this tree by hand to compare what the
# algorithm is doing. As the input has 9 entries, there will be 9
# nodes; 10 including the root node. Furthermore, each node can only
# be accessed from below by one node, so each node except the root
# will be in the image of exactly one node. So we make a pool of
# integers from 1 to 10 (note *1 below.) The input tells us that
# nothing branches to the right of nodes 5, 6, 8, 9, or 10, so by hand
# we might begin by making these keys and pointing them to zero
# (*2). Node 7 has splits (2 of them), so we look at the two entries
# after 7 in the pool of nodes, (*3) and a little thought shows that 7
# must point to 9 and 9 must point to 8 (both on the left this time.)
# Continue this procedure by using the largest nodes from the pool
# first to fill in the rest of the tree.
#############################################################################
def maketree(a):
  #if no splits occurred return trivial tree  
  if a==[]:
    return {1:[0]}
  # num of nodes = num of splits + 1 root
  m = len(a) + 1
  out = {}
  #pool creates a list of integers 1 to m
  pool = list(range(1,m+1))# (*1)

  for i in range(m, 0, -1):
    if not(i in a):
       out[i]=[0]# (*2) no splits so make them point to 0
    else:
      start = pool.index(i)
      length = a.count(i);# (*3)
      out[i] = [pool[start+length]]
      for j in range(start+length-1, start, -1):
        out[pool[j+1]].insert(0,pool[j])
      pool[start+1:start+length+1] = []
  for i in out.keys():
    if len(out[i])==1 and i!=1:
      out[i].insert(0,0)
  return out

#Here is one of the examples referenced in the explanation above.
#print(maketree([1,2,2,2,2,5,5,7,7,7,9]))
#print(maketree([1,1,1,2,3,3,4,7,7]))

################################################################################
# run
################################################################################
# NOTE: it seems that when calling you need to call run(a[:],b[:])
#       otherwise it changes them and results in an error - Aaron
#
# The main procedure; runs an entire checker game (and all splits)
# based on two input schubert conditions
#
# input:
#         a - First schubert condition
#         b - Second schubert condition
#
# output:
#         rstore - List containing every set of final red checker positions
#         tree - A hash table containing the structure of the output tree
#
# other:
#         n - Dimension of the board
#         red - List of red checkers. Becomes a queue if splits occur
#         black - List of black checkers. Determined by n, and acts as a queue
#                 for subsequent positions
#         runcount - Counts the number of times the while-loop runs. This fixes
#                    an order on the output tree.
#         tree - A list which is used to determine the tree structure. (Need an
#                example of this)
#
def run(a,b):
  #First we combine the two initial conditions into a list of checker
  #positions
  red = []
  tree = []
  n = len(a)
  for i in range(a.count(99)):  #remove all 99's
    a.remove(99)

  for i in range(n):
    if b[i] == 99 or a == []:
      red.append(99)
    else:
      red.append(a.pop())
  #Then we check for red checkers above the anti-diagonal.  If one is
  #found, give a null output (a list with n 99's and an empty dict)
  for i in range(n):
    if i+red[i] < n-1: 
      return [n*[99]], {}
  rstore = []
  black = []
  runcount = 0

  #Make the list of initial black checker positions, an anti-diagonal
  for i in range(n):
    black.append(n-i-1)

  while black != []:
    #Calls the function "game" and store the output 
    #(i.e. output = game(input))
    #print "black before->", black
    #print "red before->", red
    black, red, splitcount = game(black, red, n)
    #print "black after->", black
    #print "red after->", red
    runcount += 1
    tree.extend(splitcount*[runcount])
    #Keep the resulting red positions
    rstore.append(red[0:n])
    #Delete the computed instance
    del black[0:n]
    del red[0:n]
  tree = maketree(tree)#Make a hash table with the structure of the tree.
  return rstore, tree

#print run([99,1,2,99,4,5],[99,1,2,99,4,5])

# Aaron: 
# I just copied this from how he setup game above and took out the stuff I didn't need
# Used in newMethod.py, takes two schubert conditions and returns the list
# used in running gamePreemptive
def setupGame(first,second):
  a = first[:]
  b = second[:]
  red = []
  tree = []
  n = len(a)
  for i in range(a.count(99)):  #remove all 99's
    a.remove(99)

  for i in range(n):
    if b[i] == 99 or a == []:
      red.append(99)
    else:
      red.append(a.pop())
  #Then we check for red checkers above the anti-diagonal.  If one is
  #found, give a null output (a list with n 99's and an empty dict)
  for i in range(n):
    if i+red[i] < n-1:
      return [n*[99]], {}
  rstore = []
  black = []
  runcount = 0

  #Make the list of initial black checker positions, an anti-diagonal
  for i in range(n):
    black.append(n-i-1)
  return black,red

