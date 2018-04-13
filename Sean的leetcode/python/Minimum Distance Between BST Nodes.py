###
# DFS
# Time Complexity: O(n) 
# Space Complexity: O(h)
###
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    def inorder(self, node):
        if not node:
            return 
        self.inorder(node.left)
        if self.prev:
            self.min_dis = min(self.min_dis, node.val - self.prev.val)
        self.prev = node
        self.inorder(node.right)
        
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return -1
        self.prev = None
        self.min_dis = float('inf')
        self.inorder(root)        
        return self.min_dis
        
        