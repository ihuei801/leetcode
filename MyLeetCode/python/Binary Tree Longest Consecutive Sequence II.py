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

    def dfs(self, cur):
        if not cur:
            return 0, 0
        l_incr, l_decr = self.dfs(cur.left)
        r_incr, r_decr = self.dfs(cur.right)
        l_incr_ext = l_decr_ext = 1
        r_incr_ext = r_decr_ext = 1
        if cur.left:
            if cur.left.val == cur.val + 1:
                l_incr_ext = l_incr + 1
            if cur.left.val == cur.val - 1:
                l_decr_ext = l_decr + 1
        if cur.right:
            if cur.right.val == cur.val + 1:
                r_incr_ext = r_incr + 1
            if cur.right.val == cur.val - 1:
                r_decr_ext = r_decr + 1
        self.maxlen = max(self.maxlen, max(l_incr_ext + r_decr_ext - 1, r_incr_ext + l_decr_ext - 1))
        return max(l_incr_ext, r_incr_ext), max(l_decr_ext, r_decr_ext)

        
                                        
                            
                    