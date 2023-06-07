"""
Given the root of a binary tree, invert the tree, and return its root.
 

Example 1:

Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]

Example 2:

Input: root = [2,1,3]
Output: [2,3,1]

Example 3:

Input: root = []
Output: []
 

Constraints:

    The number of nodes in the tree is in the range [0, 100].
    -100 <= Node.val <= 100
"""
#############################################################
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
#############################################################
def invertTree1(root):
    if not root:
        return None
    
    tmp = root.left
    root.left = root.right
    root.right = tmp

    invertTree1(root=root.left)
    invertTree1(root=root.right)
    return root
#############################################################
# root = [4,2,7,1,3,6,9]
root1 = TreeNode(4)
root1.left = TreeNode(2)
root1.right = TreeNode(7)
root1.left.left = TreeNode(1)
root1.left.right = TreeNode(3)
root1.right.left = TreeNode(6)
root1.right.right = TreeNode(9)
print(root1.left.val)
invertTree1(root1)
print(root1.left.val)