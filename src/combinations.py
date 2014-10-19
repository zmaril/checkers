# nextPair computes the next lexicographic 2-Combination of elements
# input: list with or without repeats, should all be same type
# ouput: next Lexicographic pair (type list)
def nextPair(multiset,combination=None):

  array = sorted(multiset[:])

  #first combination is simply first two elements
  if len(multiset) < 2:
    return None
  if combination == None:
    return [array[0],array[1]]

  curr = combination[:]
  maxVal = array[-1] #max value curr[1] can have


  #correct input
  if curr[0] > curr[1]:
    curr[0], curr[1] = curr[1], curr[0]

  #end condition
  if curr == [array[-2],array[-1]]:
    return None

  #in case there is only one copy of maxVal which is already
  #being used by curr[0]
  if curr[0] == maxVal:
    maxVal = array[-2]

  #case change both elements
  if curr[1] == maxVal:
    loc = array.index(curr[0])
    lastTime = False
    for newVal in array[loc:]:
      if lastTime:
        curr[1] = newVal
        break
      #scan for next value
      if newVal != curr[0]:
        curr[0] = newVal
        #curr[1] should be next element in list
        #allow for one last iteration
        lastTime = True
  #case only change last element
  else:
    array.remove(curr[0])
    loc = array.index(curr[1])
    #scan for next value
    for newVal in array[loc:]:
      if newVal != curr[1]:
        curr[1] = newVal
        break

  return curr
