#see if its supposed to reappend the red at the beginning
#figure out why solutions aren't correct, if reappend always the same still not right though
#otherwise wrong




#TODO: see how gamePreemptive should handle trees (source checkergame.py)
#TODO: find source of infinite loop
from checkergame import gamePreemptive, setupGame
from combinations import nextPair,allPairs

class Result:
  def __init__(self, e, m=0, s=1, a=False):
    self.exceptions = e
    self.Matieu = m
    self.solutions = s
    self.alternating = a #may not be true

#TODO: Figure out how to make black & red lists of lists
class Key:
  def __init__(self,_n, parts = [], black = [], red = [], t=None):
    self.n = _n
    self.partitions = parts[:]
    self.startedBlack = black[:] #TODO: Figure out how to make this a list of lists
    self.startedRed = red[:]     #TODO: Figure out how to make this a list of lists
    if t == None:
      self.trees = [{}] * (len(self.startedBlack) / _n)  #TODO: Check this, it doesn't look right
    else:
      self.trees = t[:]

  # TODO:  Verify this works, check error conditions on remove and setupGame
  # define a new Key by removing the items(2) in pair form self.partitions
  # and adding the appropriate started game
  def newKeyFromPartition(self,pair):
    newKey = Key(self.n,self.partitions,self.startedBlack,self.startedRed,self.trees)
    newKey.partitions.remove(pair[0])
    newKey.partitions.remove(pair[1])
    
    black,red = setupGame(pair[0],pair[1])
    if red != {}:
      newKey.startedBlack.append(black)
      newKey.startedRed.append(red)
    else:
      return None

    return newKey

  # TODO:
  # define a new Key by advancing in game[i]
  def newKeyFromAdvancingGame(self,i):
    newKey1 = Key(self.n,self.partitions,self.startedBlack,self.startedRed,self.trees)
    #print "self.startedBlack before-> ", self.startedBlack
    #print "self.startedRed before-> ", self.startedRed
    #newKey.startedBlack,
    black, red, split = gamePreemptive(newKey1.startedBlack[i][:],newKey1.startedRed[i][:],newKey1.n)
    #need to make two keys
    if split > 0:
      black1 = black[:newKey1.n]
      red1 = red[:newKey1.n]
      black2 = black[newKey1.n:]
      red2 = red[newKey1.n:]
      newKey1.startedBlack.pop(i)
      newKey1.startedRed.pop(i)
      newKey2 = Key(self.n,newKey1.partitions,newKey1.startedBlack,newKey1.startedRed,newKey1.trees)
      newKey1.startedBlack.append(black1)
      newKey2.startedBlack.append(black2)
      newKey1.startedRed.append(red1)
      newKey2.startedRed.append(red2)
      #print "newKey1.startedBlack = ",newKey1.startedBlack
      #print "newKey1.startedRed = ",newKey1.startedRed
      #print "newKey2.startedBlack = ",newKey2.startedBlack
      #print "newKey2.startedRed = ",newKey2.startedRed
      return newKey1, newKey2
    #no split need to add new partitions tournament style
    else:
      #TODO: may need to make sure this is correct
      newKey1.startedBlack.pop(i)
      newKey1.startedRed.pop(i)
      if black != range(newKey1.n):
        print "black did not finish as [0,1,2,3,4...] ->", black
      #print "appending", red
      newKey1.partitions.append(red[:])
      return newKey1, None
    

#TODO: implement this better, maybe the way exceptions and matieu are different
def vote(results):
  if results == None or results == []:
    #print "Results are empty or None, probably not ideal"
    return Result(0,0,1,True)		#Empty result
  if len(results) == 1:
    return results[0]
  #print 'voting'
  solutions = results[0].solutions
  totExceptions = 0
  totMatieu = 0
  alternating = False
  for r in results:
    if r.solutions != solutions:
      print "r.solutions", "solutions"
    alternating = alternating or r.alternating
    #solutions = max(solutions, r.solutions)
    #if r.solutions != solutions:
      #print "These things should match", r.solutions, solutions
    totExceptions += r.exceptions
    totMatieu = r.Matieu
    #TODO: Consider breaking if alternating is true to save time!

  newResults = Result(totExceptions,totMatieu,solutions,alternating)
  return newResults

# Main function
def GG(key):
  if key == None:
    return None
  results = []
  if key.partitions != []:
    pair = nextPair(key.partitions)
  else:
    pair = None

  #Try all partitions
  while pair != None:
    newKey = key.newKeyFromPartition(pair)
    #print "newKey.startedBlack->", newKey.startedBlack
    #print "newKey.startedRed->", newKey.startedRed
    if newKey != None:
      results.append(GG(newKey))
    pair = nextPair(key.partitions,pair)
    
  count = 0
  count2 = 0
  #Try Advancing all games
  for i in range(len(key.startedBlack)):
    key2 = None
    #handle a split in the game!
    key1, key2 = key.newKeyFromAdvancingGame(i)
    #print "key1 stuff", key1.startedBlack, key1.startedRed, key1.partitions
    #if key2 != None:
    #  print "key2 stuff", key2.startedBlack, key2.startedRed, key2.partitions
    #if only one key (no split)
    if key2 == None:
      #TODO: append new partitions somehow???
      results.append(GG(key1))
    #A split occurred, must combine results
    else:
      result1 = GG(key1)
      result2 = GG(key2)
      if result1.solutions == result2.solutions:
        count+= 1;
      else:
        count2 +=1;
        
        #print "result1.solutions = ", result1.solutions, " result2.solutions = ", result2.solutions
      combinedResult = Result( 
        result1.exceptions + result2.exceptions,
        result1.Matieu + result2.Matieu,
        result1.solutions + result2.solutions
      )
      if ((result1.alternating and result2.alternating) and
          (result1.solutions != result2.solutions)):
        combinedResult.alternating = True
      results.append(combinedResult)

      #print "count = ", count, "count2 = ", count2
  #print "Ending a level ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
  #print "Length of results", len(results)
  #print "size of results", len(results)
  print '-------------------------------------------------------------------------'
  if len(results) > 1:
    for r in results:
      print r.solutions
  print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
  return vote(results)
  

def testMethod():
  #a = [[99,99,2,3,99,99,6,7]]
  #print(tournament(4*a, 1))
  #a = [[99,1,99,3]]
  #a = [[99,99,99,3,99,5]]
  #a = [[99,99,99,3,99,5]]
  #a = [[99,99,2,99,4,99,6],[99,99,99,3,4,99,6]]
  #b = [[99,99,99,3,99,5,6]]
  #k = Key(7,a + 7*b)
  #k = Key(4, 4*a)
  k = Key(6,[[99,99,99,3,99,5]]*2 + [[99,99,2,99,99,5]]*3)
  #k = Key(5, [[99,99,2,99,4]]*6)# + [[99,1,99,99,4]]*1)
  result = GG(k)
  print "results"
  print "solutions", result.solutions
  print "exceptions", result.exceptions
  print "Matieu", result.Matieu

print testMethod()

