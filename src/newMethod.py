from checkergame import gamePreemptive, setupGame
from combinations import nextPair

class Result:
  __slots__ = ['exceptions','Matieu','solutions','alternating']
  def __init__(self, e, m=0, s=1, a=False):
    self.exceptions = e
    self.Matieu = m
    self.solutions = s
    self.alternating = a #may not be true

class Key:
  __slots__ = ['n','partitions','startedGames','trees']
  def __init__(self,_n, parts = [], games = [], t=None):
    self.n = _n
    self.partitions = sorted(parts[:])
    self.startedGames = sorted(games[:])
    if t == None:
      self.trees = [{}] * (len(self.startedGames) / _n)  #TODO: Check this, it doesn't look right
    else:
      self.trees = t[:]

  def __eq__(self,other):
      if other == None:
         return False
      n = self.n == other.n
      p = self.partitions == other.partitions
      s = self.startedGames == other.startedGames
      return n and p and s

  def __hash__(self):
    p = tuple(map(tuple,self.partitions))
    gs = []
    for x in self.startedGames:
        gs.append(tuple(map(tuple,x)))
    gs = tuple(gs)
    return hash((self.n,p,gs))

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
    black, red, split = gamePreemptive(newKey1.startedGames[i][0][:],
                                       newKey1.startedGames[i][1][:],
                                       newKey1.n)
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

def GG2(key):
  result = None

  if key.partitions != []:
    pair = nextPair(key.partitions)
  else:
    pair = None

  #Try all partitions
  dontFit = False  #flag to alert if the partitions do not fit together

  while pair != None:
    newKey = key.newKeyFromPartition(pair)
    if newKey != None:
      result = GG2(newKey)
    else:
      dontFit = True

      #TODO:if GG(newKey).alternating = True!, return that result?

    if result != None and result.alternating == True:
      return result

    pair = nextPair(key.partitions,pair)

  #Try Advancing all games
  combinedResult = None
  for i in range(len(key.startedGames)):
    result = None
    key2 = None
    #handle a split in the game!
    key1, key2 = key.newKeyFromAdvancingGame(i)

    if key2 == None:
      result = GG2(key1)

      if result != None and result.alternating == True:
        return result
    else:
      result1 = GG2(key1)
      result2 = GG2(key2)


      combinedResult = Result(
        result1.exceptions + result2.exceptions,
        result1.Matieu + result2.Matieu,
        result1.solutions + result2.solutions
      )


          #to the second line should I add "or result1.solutions == 0?" I think so.
      if ((result1.alternating and result2.alternating) and
          (result1.solutions != result2.solutions  or result1.solutions == 0 or result1.solutions == 1)):
        combinedResult.alternating = True
      elif result1.solutions == result2.solutions:
        if result1.solutions == 6:
          combinedResult.Matieu += 1
        combinedResult.exceptions += 1
      #TODO:if combinedResult.alternating == True, return that result?
      if combinedResult.alternating == True:
        return combinedResult
      #results.append(combinedResult)
  if combinedResult != None:
    return combinedResult
  if result != None:
    return result
  if result == None and dontFit:
    return Result(0,0,0,True)
  if result == None and dontFit == False:
    return Result(0,0,1,True)
  return result

class GGMemoize:
    def __init__(self, f):
        self.f = f
        self.memo = {}
    def __call__(self, *args):
      arg = args[0]
      if len(self.memo) >= 100000:
          self.memo = {}
          print "DROPPPPP THE CACHE"
      if not arg in self.memo:
        self.memo[arg] = self.f(arg)

      return self.memo[arg]

GG2=GGMemoize(GG2)

(+ 177 55 222 36 167)
