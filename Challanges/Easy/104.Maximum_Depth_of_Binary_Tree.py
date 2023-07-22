""" https://leetcode.com/problems/maximum-depth-of-binary-tree/description/
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.


Example 1:
https://assets.leetcode.com/uploads/2020/11/26/tmp-tree.jpg

Input: root = [3,9,20,null,null,15,7]
Output: 3

Example 2:

Input: root = [1,null,2]
Output: 2

 
Constraints:

    The number of nodes in the tree is in the range [0, 104].
    -100 <= Node.val <= 100
"""
#################################################################
# Definition for a binary tree node.
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

def maxDepth(self, root):
  if root == None:
    return 0

  right, left = 0,0
  if root.left != None:
    left = self.maxDepth(root.left) + 1
  else:
    left += 1
  
  if root.right != None:
    right = self.maxDepth(root.right) + 1
  else:
    right += 1

  return max(left, right)