from checkergame import run
# Creates a recursive tree structure to compute Vakil's criterion
# for a tree given in Chris' Hash form


class VakilNode:
  def __init__(self,name,intersection):
    self.nodesAbove = intersection
    self.left = None
    self.right = None
    self.name = name  #just to help me see if I'm doing it right

  #depth first print of nodeNames, to test structure
  def printSubTree(self):
    if self.left != None:
      self.left.printSubTree()
    print self.name, '->', self.nodesAbove
    if self.right != None:
      self.right.printSubTree()


  def vakil(self):
    if self.name == 0:
      return True, self.nodesAbove

    if self.left != None:
      leftPassed, l = self.left.vakil()

    if self.right != None:
      rightPassed, r = self.right.vakil()
    else:
      rightPassed, r = True, 0  #since root doesn't have a right
    # given condition for vakil's test
    vakilCondition = (l == 1 and r == 1) or (l != r) or (l == 0 and r == 0)

    # has to have already passed left, and right and pass here
    passed = leftPassed and rightPassed and vakilCondition
    self.nodesAbove = l + r

    return passed, self.nodesAbove
 


#Tree is holds root of VakilTree in self.root
class VakilTree:
  
  def replaceLeaves(self,node):
    if node.left == None:
      node.left = VakilNode(0,self.remainingMults.pop(0))
    else:
      self.replaceLeaves(node.left)
    if node.right == None:
      if len(self.remainingMults) != 0:  #so that it doesn't add out of bounds
        node.right = VakilNode(0,self.remainingMults.pop(0))
    else:
      self.replaceLeaves(node.right)



  def __init__(self,tree,mults=None):
    self.hashTree = tree
    nodeList = [None]

    if mults == None:
      mults = [1] * len(tree)
    
    self.remainingMults = mults[:]
    #create the correct number of nodes
    for i in range(len(tree)):
      nodeList.append(VakilNode(i+1,1))

    #create tree structure
    for i in tree:
      l = tree[i][0]
      nodeList[i].left = nodeList[l]
      if i != 1:
        r = tree[i][1]
      else:
        r = 0
      nodeList[i].right = nodeList[r]

    self.root = nodeList[1]
    self.replaceLeaves(self.root)

  def printTree(self):
    self.root.printSubTree()

  def vakil(self):
    #call vakil from vakilNode above root and only returns True/False
    return self.root.left.vakil()[0]


# This will be the function you use
# input = a hash style tree like the one returned from run
# output = boolean result of vakil's test
def vakilTest(tree,mults=None):
  if tree == {} or tree == {1: [0]}:
    return True   #TODO: ask if this is true or false
  vt = VakilTree(tree,mults)
  return vt.vakil()


#vt = VakilTree({1:[2], 2:[3,4], 3:[0,0], 4:[0,0]},[8,7,6,5])
#vt.printTree()
#while the numberings don't make sense, the trees do


