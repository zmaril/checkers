from tournament import *

# Unless otherwise stated below, a partition is written as in the following
# example (which I refer to as 'multiplicity form'; there might be a more
# standard word): One partition of 18 is 1+1+1+2+3+4+6, which would be denoted
# by [3,1,1,1,0,1] (three 1's, one 2, one 3, one 4, zero 5's, 1 six).

################################################################################
# makeproblem
################################################################################
#
# Returns a Schubert problem (to use in checkergame.py and tournament.py) given
# the following information
#
#   1.) k and n (working in G(k,n))
#   2.) A partition of k*(n-k) (the 'type' of the problem)
#   3.) A set of shapes for each part size in item 1 (a list of partitions)
#   4.) A list specifying the number of shapes from item 2
#
# Example:
#
# The following data encodes the problem
# []^12 * []^4 * [][] * [][] * [][][]
#         []            [][]   []       in G(5,11)
#
# k, n = 5, 11
# problem_type = [12,5,0,2]
# shapes = {1:[[1]], 2:[[2],[0,1]], 4:[[4],[2,1],[0,2],[1,0,1],[0,0,0,1]]}
# shape_type = {1:[12], 2:[4,1], 4:[0,0,1,1,0]}
#
# makeproblem[0] is human readable partition notation while makeproblem[1] is
# checker input (for tournament and/or checkergame routines, and more recently intersectionNum)
#
def makeproblem(k, n, problem_type, shapes, shape_type):
  out_problem = []
  for i in range(len(problem_type)):
    if problem_type[i] == 0: continue
    #The following checks for bad input
    error1 = 'Not enough shapes specified in shape_type[{0}]'.format(i)
    error2 = 'Length mismatch in shapes[{0}] and shape_type[{0}]'.format(i)
    if sum(shape_type[i+1]) != problem_type[i]:
      raise ValueError(error1)
    if len(shape_type[i+1]) != len(shapes[i+1]):
      raise ValueError(error2)
    #Now we attach the schubert conditions to 'out_problem'
    for j in range(len(shape_type[i+1])):
      #Append the correct number of copies of shapes[i+1][j] to the problem
      out_problem = out_problem + shape_type[i+1][j]*[shapes[i+1][j]]
  out_checkers = out_problem[:]
  for i, item in enumerate(out_checkers):
    out_checkers[i] = partitions2checkers(k, n, item)
  return out_problem, out_checkers

#k,n = 5,11
#problem_type = [12,5,0,2]
#shapes = {1:[[1]], 2:[[2],[0,1]], 4:[[4],[2,1],[0,2],[1,0,1],[0,0,0,1]]}
#shape_type = {1:[12], 2:[4,1], 4:[0,0,1,1,0]}
#print(makeproblem(k,n,problem_type,shape_type))


################################################################################
# next_partition
#########################################################################
#######
#
# input is a partition in multiplicity form, m is max size of part. Returns the
# next lexicographic partition or [] if there are no more partitions.
#
def next_partition(in_part, m):
  out = in_part[:]
  j=1
  a=out[0]
  while a < j+1:
    if j == m-1:
      return []
    try:
      a += (j+1) * out[j]
    except IndexError:
      return []
    j += 1
  try:
    out[j] += 1
  except IndexError:
    out.append(1)
  out[0] = a-j-1
  for i in range(1,j):
    out[i]=0
  return out

################################################################################
# next_partition_hind
################################################################################
#
# Takes a partition (in multiplicity form) and returns the next partition with
# the same number of parts. Algorithm is due to Hindenburg (1778). First write
# the sum in increasing order, say n = a_1 + ... + a_m; then find the rightmost
# element differing from a_m by at least 2, call this element a_i. Then replace
# a_i, a_{i+1}, ..., a_{m-1} with 1+a_i. Finally, adjust a_m so that it is
# still a partition of n. Use this for generating the sequence of sizes in a
# Schubert problem, and partgen for generating each individual tableau
#
# The order of this algorithm is determined as follows: If a and b are
# partitions in multiplicity form, then go to the leftmost i such that a[i] and
# b[i] differ. Then a < b if a[i] > b[i] and vice-versa. Thus, the partition
# with as many 1's possible is always the first lexicographic partition (in this
# ordering)
#
def next_partition_hind(in_part):
  out = in_part[:]
  max = len(out)-1
  check = list(out)
  while check[0]==0:
    check.pop(0)
  if len(check)<3:
    return []
  for i in range(max, -1, -1):
    if max >= i+2 and out[i]!=0:
      break
  count = sum(out[i+1:])
  b=[(j+1)*out[j] for j in range(0, max+1)]
  total = sum(b[i+1:]) + i + 1
  out[i] -= 1
  out[max-1] = 0
  out[max] = 0
  out[i+1] = count
  new = total - (i+2)*count
  try: out[new-1] += 1
  except IndexError:
    out.extend((new-max-1)*[0])
    out[new-1] = 1
  if out[-1]==0: out[new:] = []
  return out

################################################################################
# get_all_parts
################################################################################
#
# Generate all partitions with at most k parts where each part is at most n-k.
# This is used to create a dictionary of all possible schubert conditions on a
# grassmannian G(k,n); these conditions are iterated over in next_problem.
#
def get_all_parts(k, n):
  partitions = {1:[[1]]}
  for i in range(2,k*(n-k)+1):
    partitions_of_i = []
    to_add = [i]
    while to_add != []:
      if sum(to_add) <= k:
        partitions_of_i.append(to_add)
      to_add = next_partition(to_add, n-k)
    partitions[i] = partitions_of_i
  return partitions

################################################################################
# next_shape_type
################################################################################
#
# In the 'makeproblem' routine, we needed a list of possible partitions for each
# index with nonzero entry in 'problem_type'. Then in 'shape_type' we have a
# list of multiplicities for which partitions actually occured.
#
# A list in 'shape_type' then can be any list of nonnegative integers. This code
# takes such a list and returns the next list (in dictionary order) with the
# same sum.
#
# Here is this routine in pseudocode:
#   Subtract 1 from rightmost.
#   If rightmost is >=0, do
#     add 1 to the integer 1 to the left
#   If rightmost is -1, do
#     Add second rightmost nonzero to rightmost
#     Change that number to zero
#     Add 1 to the left of previous number
#
def next_shape_type(arr):
  if arr == len(arr)*[0] or len(arr) < 2:
    return []
  arr[-1] -= 1
  if arr[-1] >= 0:
    arr[-2] += 1
  elif arr[-1] == -1:
    i = -2
    while arr[i] == 0:
      i -= 1
    arr[-1] += arr[i]
    arr[i] = 0
    try: arr[i-1] += 1
    except IndexError: return []
  elif arr[-1] < -1:
    raise ValueError('Bad input')
  return arr

################################################################################
# next_problem
################################################################################
#
# In the make_problem routine, we take the following information and construct
# a problem. This routine takes the same information (defining a problem) and
# returns the set of information defining the next lexicographic problem with
# the same number of conditions.
#
#   1.) k and n (working in G(k,n))
#   2.) A partition of k*(n-k) (the 'type' of the problem)
#   3.) A master list of schubert conditions possible on G(k,n) (this is a
#       dictionary generated beforehand
#   4.) A list specifying the number of shapes from item 2
#
# For instance, given the following information,
#k,n = 5,11
#problem_type = [12,5,0,2]
#shape_type = {1:[12], 2:[4,1], 4:[0,0,1,1,0]}
# we want next_problem to output
# problem_type = [12, 5, 0, 2]
# shape_type = {1:[12], 2:[4,1], 4:[0,0,2,0,0]}
#
def next_problem(k, n, in_prob_type, shapes, shape_type):
  prob_type = in_prob_type[:]
  i = len(prob_type)
  shape_type[i] = next_shape_type(shape_type[i])
  while shape_type[i] == []:
    shape_type[i] = len(shapes[i])*[0]
    shape_type[i][-1] = prob_type[i-1]
    try:
      shape_type[i-1] = next_shape_type(shape_type[i-1])
    except KeyError:
      prob_type = next_partition_hind(prob_type)
      shape_type = {}
      for j in range(1, len(prob_type)+1):
        shape_type[j] = len(shapes[j])*[0]
        shape_type[j][-1] = prob_type[j-1]
      return prob_type, shape_type
    i -= 1
  return prob_type, shape_type
