# rtest
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
def rtest(x1, y1, x2, y2, R, n): #PASS BY REFERENCE 
  #print(x1,y1,x2,y2,R,n)
  greek=2; roman=2; sp=0
  #Find the critical row, "cr"
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
        R.extend(rts[0:n]) #TODO: This is still weird.
        sp = 1#Flag that indicates that split occured
  if roman == 2 and greek == 0:
    R[x1] = R[cr]
    R[cr] = 99
    #print(R,sp) 
  return R, sp

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

