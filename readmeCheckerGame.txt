
################################
# Examples
################################
#
# Suppose we are in G(2,4). Then we have the decomposition:
#   [] * [] =  [] + [][]
#              []
#   In the code, this would be run([99,1,99,3],[99,1,99,3]). The 99's are single horizontal steps (left) and non-99's are single
#   vertical steps (down) when you draw the boxes given the input. The output is what we expect:
#   [[99, 1, 2, 99], [0,99, 99, 3]] (corresponding to [] and [][] respectively)
#                                                     []
#   and we also get {1:[2], 2:[0,0]}. This tells you the tree structure. Node one points to node two, and node two
#   points to the two conditions we end up with. The details of node numbering are in the separate documentation I'm working on right now.
#
# In G(2,8), we have:
#   [][][] * [][][] = [][][] + [][][][] + [][][][][] + [][][][][][]
#                     [][][]   [][]       []
#   In code, this is run([99,99,99,3,99,99,99,7],[99,99,99,3,99,99,99,7]),
#   and the output is: [[99, 99, 99, 3, 4, 99, 99, 99], [99, 99, 2, 99, 99, 5, 99, 99], 
#   [99, 1, 99, 99, 99, 99, 6, 99], [0, 99, 99, 99, 99, 99, 99, 7]] as the RHS of the decomposition above,
#   with the tree {1: [2], 2: [3, 0], 3: [4, 0], 4: [0, 0]}
#
# In G(4,8), we have (You may want to do this by hand to make sure since I don't know G(k,n) by hand for k>2)
#   [][] * [][] = [][] + [][][] + [][][] + [][][][] + [][][][] + [][][][]
#   [][]   [][]   [][]   [][]     [][][]   [][]       [][][]     [][][][]
#                 [][]   [][]     []       [][]       []
#                 [][]   []       []
#   Input is: run([99,99,2,3,99,99,6,7],[99,99,2,3,99,99,6,7])
#   Output is:[[99, 99, 2, 3, 4, 5, 99, 99], [99, 1, 99, 3, 4, 99, 6, 99], [99, 1, 2, 99, 99, 5, 6, 99],
#   [0, 99, 99, 3, 4, 99, 99, 7], [0, 99, 2, 99, 99, 5, 99, 7], [0, 1, 99, 99, 99, 99, 6, 7] with the tree
#   {1: [2], 2: [3, 4], 3: [0, 0], 4: [0, 5], 5: [6, 0], 6: [0, 0]}
#
#print(run([99,1,99,3],[99,1,99,3]))
#print(run([99,99,99,3,99,99,99,7],[99,99,99,3,99,99,99,7]))
