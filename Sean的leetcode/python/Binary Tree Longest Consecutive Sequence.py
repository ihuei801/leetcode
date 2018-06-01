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
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        self.maxlen = 0
        self.dfs(root)
        return self.maxlen
    
    def dfs(self, root):
        if not root:
            return 0
        left_incr = self.dfs(root.left)
        right_incr = self.dfs(root.right)
        l_incr = r_incr = 1
        if root.left and root.val + 1 == root.left.val:
            l_incr = left_incr + 1
        if root.right and root.val + 1 == root.right.val:
            r_incr = right_incr + 1
        self.maxlen = max(self.maxlen, max(l_incr, r_incr))
        return max(l_incr, r_incr)
        
        
               
# pre-order
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        self.max_len = 0
        self.dfs(root, None, 0)
        return self.max_len
    def dfs(self, root, parent, l):
        if not root:
            return 
        if parent and parent.val + 1 == root.val:
            l += 1
        else:
            l = 1
        self.max_len = max(self.max_len, l)
        self.dfs(root.left, root, l)
        self.dfs(root.right, root, l)     

        
        