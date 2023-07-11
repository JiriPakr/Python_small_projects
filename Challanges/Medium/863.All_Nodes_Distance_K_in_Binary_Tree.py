"""
Given the root of a binary tree, the value of a target node target, and an integer k, return an array of the values of all nodes that have a distance k from the target node.

You can return the answer in any order.

 
Example 1:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, k = 2
Output: [7,4,1]
Explanation: The nodes that are a distance 2 from the target node (with value 5) have values 7, 4, and 1.

Example 2:

Input: root = [1], target = 1, k = 3
Output: []


Constraints:

    The number of nodes in the tree is in the range [1, 500].
    0 <= Node.val <= 500
    All the values Node.val are unique.
    target is the value of one of the nodes in the tree.
    0 <= k <= 1000


 Definition for a binary tree node.
 """
class TreeNode:
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None

import collections
#####################################################
def distanceK(root: TreeNode, target: TreeNode, k: int):
  graph = collections.defaultdict(list)

  def build_graph(cur, parent):
    if cur and parent:
      graph[cur.val].append(parent.val)
      graph[parent.val].append(cur.val)
    if cur.left:
      build_graph(cur.left, cur)
    if cur.right:
      build_graph(cur.right, cur)
  build_graph(root, None)

  answer = []
  visited = set([target.val])

  def dfs(cur, distance):
    if distance == k:
      answer.append(cur)
      return
    
    for neighbor in graph[cur]:
      if neighbor not in visited:
        visited.add(neighbor)
        dfs(neighbor, distance + 1)
    
    dfs(target.val, 0)

    return answer
  #####################################################