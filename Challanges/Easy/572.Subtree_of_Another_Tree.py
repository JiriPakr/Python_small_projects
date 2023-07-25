"""
https://leetcode.com/problems/subtree-of-another-tree/description/
Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.

 

Example 1:
https://assets.leetcode.com/uploads/2021/04/28/subtree1-tree.jpg

Input: root = [3,4,5,1,2], subRoot = [4,1,2]
Output: true

Example 2:
https://assets.leetcode.com/uploads/2021/04/28/subtree2-tree.jpg

Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
Output: false

 

Constraints:

    The number of nodes in the root tree is in the range [1, 2000].
    The number of nodes in the subRoot tree is in the range [1, 1000].
    -104 <= root.val <= 104
    -104 <= subRoot.val <= 104


"""
###########################################################################
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root, subRoot) -> bool:
        if not root:
            return False

        if not subRoot:
            return True

        if self.sameTree(root, subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def sameTree(self, r, s):
        if not r and not s:
            return True
        if r and s and r.val == s.val:
            return self.sameTree(r.left, s.left) and self.sameTree(r.right, s.right)
        return False        