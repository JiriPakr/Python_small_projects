""" https://leetcode.com/problems/balanced-binary-tree/

Given a binary tree, determine if it is height-balanced.

Height-Balanced - >
A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.

 
Example 1:
https://assets.leetcode.com/uploads/2020/10/06/balance_1.jpg

Input: root = [3,9,20,null,null,15,7]
Output: true

Example 2:
https://assets.leetcode.com/uploads/2020/10/06/balance_2.jpg

Input: root = [1,2,2,3,3,null,null,4,4]
Output: false

Example 3:

Input: root = []
Output: true


Constraints:

    The number of nodes in the tree is in the range [0, 5000].
    -104 <= Node.val <= 104
"""
###################################################################
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isBalanced(root) -> bool:

  def dfs(root):
    if not root:
      return [True, 0]
    
    left, right = dfs(root.left), dfs(root.right)
    balanced = (left[0] and right[0] and abs(left[1] - right[1]) <= 1)

    return [balanced, max(left, right) + 1]
      
  return dfs(root)[0]
      
