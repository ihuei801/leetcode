###
# Tree
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
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        self.max_len = 0
        self.dfs(root)
        return self.max_len 
    
    def dfs(self, root):
        if not root:
            return 0
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        left_ext = 0
        right_ext = 0
        if root.left and root.left.val == root.val:
            left_ext = left + 1
        if root.right and root.right.val == root.val:
            right_ext = right + 1
        self.max_len = max(self.max_len, left_ext + right_ext)
        return max(left_ext, right_ext)
        
        