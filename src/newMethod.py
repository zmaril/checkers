#see if its supposed to reappend the red at the beginning
#figure out why solutions aren't correct, if reappend always the same still not right though
#otherwise wrong
import inspect

class GGMemoize:
    def __init__(self, f):
        self.f = f
        self.memo = {}
    def __call__(self, *args):
      arg = args[0]
#      print("arg")
      p = tuple(map(tuple,arg.partitions))
#      print("startedGames",arg.startedGames)
      gs = tuple(map(lambda x: tuple(map(tuple,x)),arg.startedGames))
      pgs = (p,gs)
#      print(pgs)
      if not pgs in self.memo:
        # print("args")
        # print(p)
        # print(b)
        # print(r)
        self.memo[pgs] = self.f(arg)
      return self.memo[pgs]

#TODO: see how gamePreemptive should handle trees (source checkergame.py)
#TODO: find source of infinite loop
from checkergame import gamePreemptive, setupGame
from combinations import nextPair,allPairs

class Const:
  def __init__(self):
    self.count = 0


class Result:
  def __init__(self, e, m=0, s=1, a=False):
    self.exceptions = e
    self.Matieu = m
    self.solutions = s
    self.alternating = a #may not be true

#TODO: Figure out how to make black & red lists of lists
class Key:
  def __init__(self,_n, parts = [], games = [], t=None):
    self.n = _n
    self.partitions = parts[:]
    self.startedGames = games
    if t == None:
      self.trees = [{}] * (len(self.startedGames) / _n)  #TODO: Check this, it doesn't look right
    else:
      self.trees = t[:]

  def __eq__(self,other):
      if other == None:
         return False 
      print(self,other)
      n = self.n == other.n
      p = self.partitions == other.partitions
      s = self.startedGames == other.startedGames
      return n and p and s
  
  # TODO:  Verify this works, check error conditions on remove and setupGame
  # define a new Key by removing the items(2) in pair form self.partitions
  # and adding the appropriate started game
  def newKeyFromPartition(self,pair):
    newKey = Key(self.n,self.partitions,self.startedGames,self.trees)
    newKey.partitions.remove(pair[0])
    newKey.partitions.remove(pair[1])
    
    black,red = setupGame(pair[0],pair[1])
	
    if red != {}:
      newKey.startedGames.append((black,red))
    else:
      return None

    return newKey

  # TODO:
  # define a new Key by advancing in game[i]
  def newKeyFromAdvancingGame(self,i):
    newKey1 = Key(self.n,self.partitions,self.startedGames,self.trees)
    print(self.n,self.partitions,self.startedGames,self.trees)
    try:
      black, red, split = gamePreemptive(newKey1.startedGames[i][0][:],
                                         newKey1.startedGames[i][1][:],
                                         newKey1.n)
    except IndexError:
      print(i,newKey1.startedGames)
    #need to make two keys
    if  split > 0:
      black1 = black[:newKey1.n]
      red1 = red[:newKey1.n]
      black2 = black[newKey1.n:]
      red2 = red[newKey1.n:]
      newKey1.startedGames.pop(i)
      newKey2 = Key(self.n,newKey1.partitions,newKey1.startedGames,newKey1.trees)
      newKey1.startedGames.append((black1,red1))
      newKey2.startedGames.append((black2,red2))
      return newKey1, newKey2
    #no split need to add new partitions tournament style
    else:
      #TODO: may need to make sure this is correct
      newKey1.startedGames.pop(i)
      newKey1.partitions.append(red[:])
      return newKey1, None
    

def vote(results):
  results = [x for x in results if x != None]
  if results == []:
    return Result(0,0,1,True)		#Empty result
  if len(results) == 1:
    return results[0]


  solutions = results[0].solutions
  totExceptions = 0
  totMatieu = 0
  alternating = results[0].alternating

  for r in results:
    alternating = (alternating or r.alternating)
    totExceptions += r.exceptions
    totMatieu = r.Matieu
    #TODO: Consider breaking if alternating is true to save time!

  newResult = Result(totExceptions,totMatieu,solutions,alternating)
  return newResult

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
    if newKey != None:
      results.append(GG(newKey))
      #TODO:if GG(newKey).alternating = True!, return that result?
    else:
      results.append(None)
    pair = nextPair(key.partitions,pair)
    
  #Try Advancing all games
  for i in range(len(key.startedGames)):
    key2 = None
    #handle a split in the game!
    key1, key2 = key.newKeyFromAdvancingGame(i)
    
    if key2 == None:
      results.append(GG(key1))
      #TODO:if GG(newKey).alternating = True!, return that result?
    #A split occurred, must combine results
    else:
      result1 = GG(key1)
      result2 = GG(key2)
      
	  
      combinedResult = Result( 
        result1.exceptions + result2.exceptions,
        result1.Matieu + result2.Matieu,
        result1.solutions + result2.solutions
      )
	  		  
      if ((result1.alternating and result2.alternating) and
          (result1.solutions != result2.solutions or result1.solutions == 1)):
        combinedResult.alternating = True
      elif result1.solutions == result2.solutions:
        if result1.solutions == 6:
          combinedResult.Matieu += 1
        combinedResult.exceptions += 1
      #TODO:if combinedResult.alternating == True, return that result?
      results.append(combinedResult)

#  for result in results:
#    if result.solutions == 4:
#	  print inspect.getmembers(key)
#	  for result in results:
#	      print result.solutions
  return vote(results)
  
GG=GGMemoize(GG)

def testKnownFailures4_8():
  single = [[99,99,99,3,99,5,6,7]]
  twobytwo = [[99,99,2,3,99,99,6,7]]
  threebyone = [[99,99,99,3,4,5,99,7]]
  onebythree = [[99,1,99,99,99,5,6,7]]
  uprightdomino = [[99,99,99,3,4,99,6,7]]
  otherdomino =   [[99,99,2,99,99,5,6,7]]

  keys = []
  #keys.append(Key(8,single*16))
  #keys.append(Key(8,twobytwo + single*12))
  #keys.append(Key(8,threebyone + onebythree + single * 10))
  #keys.append(Key(8,twobytwo*2 + single*8))


  #keys.append(Key(8,[[99,1,2,3,99,99,99,7]] + single * 7))
  keys.append(Key(8,[[99,99,2,3,4,99,99,7]] + uprightdomino + otherdomino*4))
  #keys.append(Key(8,[[99,2,3,99,99,99,6,7]] + uprightdomino*4 + otherdomino))
  #keys.append(Key(8,[[99,1,99,3,99,5,99,7]]*2 + uprightdomino + otherdomino))
  #keys.append(Key(9,onebythree*4 + uprightdomino + otherdomino))
  for k in keys:
    result = GG(k)
    print "results"
    print "solutions", result.solutions
    print "alternating", result.alternating
    print "exceptions", result.exceptions
    print "Matieu", result.Matieu
    print '------------------------------------------------------'


  #a = [[99,99,2,3,99,99,6,7]]
  #print(tournament(4*a, 1))
  #a = [[99,1,99,3]]
  #k = Key(4, 4*a)
  #a = [[99,99,2,99,4]]
  #b = [[99,1,99,99,4]]
  #k = Key(5,6*a)
  #k = Key(5,4*a + [[99,99,2,3,99]])
  #k = Key(5,2*a + 2*b)
  #a = [[99,99,99,3,99,5]]
  #a = [[99,99,99,3,99,5]]
  #a = [[99,99,2,99,4,99,6],[99,99,99,3,4,99,6]]
  #b = [[99,99,99,3,99,5,6]]
  #k = Key(7,a + 7*b)
  #k = Key(6,[[99,99,99,3,99,5]]*2 + [[99,99,2,99,99,5]]*3)
  #k = Key(5, [[99,99,2,99,4]]*6)# + [[99,1,99,99,4]]*1)


#testKnownFailures4_8()
