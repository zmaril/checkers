################################################################################
# More Examples
################################################################################
#
# Example 1. This is the problem of four lines, i.e. [] * [] * [] * [] in G(2,4)
#a = [[99,1,99,3]]
#print(tournament(4*a, 1))
#
# The answer is 2, and the output of the code verifies this.

# Example 2. This is a problem with exceptional geometry.
# In Young diagrams, it is [][] * [][] * [][] * [][] = 6 in G(4,8)
#                          [][]   [][]   [][]   [][]
# and the input is:
#a = [[99,99,2,3,99,99,6,7]]
#print(tournament(4*a, 1))
# The code gives the correct answer of 6. This problem fails Vakil's criterion
# at the base of the tree.

# Example 3. This is the problem {2,1}*{1,1}*{1}^7 in G(3,7)
# In Young diagrams, [][] * [] * []^7 = 77
#                    []     []
# input:
#a = [[99,99,2,99,4,99,6],[99,99,99,3,4,99,6]]
#b = [[99,99,99,3,99,5,6]]
#print(tournament(a + 7*b, 1))
# output: 77

# Example 4. This is the problem {1,1}*{2}*{1}^12 in G(4,8)
#a = [[99,99,99,3,4,99,6,7],[99,99,2,99,99,5,6,7]]
#b = [[99,99,99,3,99,5,6,7]]
#print(tournament(a + 12*b, 1))
