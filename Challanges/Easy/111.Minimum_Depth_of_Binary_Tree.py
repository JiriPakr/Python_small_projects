"""
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.


Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: 2

Example 2:

Input: root = [2,null,3,null,4,null,5,null,6]
Output: 5


Constraints:

    The number of nodes in the tree is in the range [0, 105].
    -1000 <= Node.val <= 1000
"""
import collections
##################################################################
#Definition for a binary tree node.
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
      self.val = val
      self.left = left
      self.right = right

# DFS
def minDepth(root: TreeNode) -> int:
  def dfs(root: TreeNode) -> int:
      if not root:
          return 0

      if not root.left:
          return 1 + dfs(root.right)
      elif not root.right:
          return 1 + dfs(root.left)

      return 1 + min(dfs(root.left), dfs(root.right))
  return dfs(root)
############################################################  
# BFS
def minDepth(root: TreeNode) -> int:
  if not root:
      return 0
  
  queue = collections.deque()
  queue.append(root)
  depth = 0

  while queue:
      size = len(queue)
      depth += 1

      for _ in range(size):
          node = queue.popleft()

          if not node.left and not node.right:
              return depth

          if node.left:
              queue.append(node.left)
          
          if node.right:
              queue.append(node.right)
  return 0
############################################################
root1 = [3,9,20,None,None,15,7]

print(minDepth(root1))