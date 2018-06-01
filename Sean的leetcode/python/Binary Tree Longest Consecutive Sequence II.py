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
            return (0, 0)
        left_incr, left_decr = self.dfs(root.left)
        right_incr, right_decr = self.dfs(root.right)
        l_incr = l_decr = r_incr = r_decr = 1
        if root.left:
            if root.val + 1 == root.left.val:
                l_incr = left_incr + 1
            elif root.val - 1 == root.left.val:
                l_decr = left_decr + 1
        if root.right:
            if root.val + 1 == root.right.val:
                r_incr = right_incr + 1
            elif root.val - 1 == root.right.val:
                r_decr = right_decr + 1
        self.maxlen = max(self.maxlen, l_incr + r_decr - 1, l_decr + r_incr - 1)
        return max(l_incr, r_incr), max(l_decr, r_decr)

        
                                        
                            
                    