from checkergame import run
#print run([99,1,99,3,99,5,99,99],[99,99,99,3,99,5,99,7])[1]

#
  
#iterative vakil test!
def vakil_test(hash_tree,mults=None):
  if hash_tree == {} or hash_tree == {1:[0]}:
    return True
  if mults == None:
    mults = [1]*len(hash_tree)
  stack = [1]  #simulate stack order of recursion
  visited = set() #avoid repeating nodes
  new_mults = []
  passed = True

  while stack != []:
    node = stack.pop(0)
    if node not in visited or node == 0:
      visited.add(node)
      #print node
      if node == 0:
        continue
      #setting up a post order traversal
      stack = hash_tree[node] + [node] + stack
    else:
      if node != 1:
        #Leaf nodes take the value from mults since they are new,
        #nonleaves come from things that have already been calculated
        if hash_tree[node][0] == 0:
          mults_l = mults.pop(0)
        else:
          mults_l = new_mults.pop(0)
        if hash_tree[node][1] == 0:
          mults_r = mults.pop(0)
        else:
          mults_r = new_mults.pop(0)
        
        passed = passed and (mults_l != mults_r or mults_r == 1 or mults_r == 0)
        new_mults.insert(0,mults_l+mults_r)

  return passed


#print vakil_test({1:[2],2:[3,0],3:[4,0],4:[0,0]},[1,1,1,1])
