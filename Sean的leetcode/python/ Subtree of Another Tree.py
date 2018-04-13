###
# DFS
# Time Complexity: O(m+n)
# Space Complexity: O(m+n)
########################################
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if not t:
            return True
        if not s:
            return False
        s_re = []
        t_re = []
        self.dfs(s, s_re)
        s_str = ',' + ','.join(s_re)
        self.dfs(t, t_re)
        t_str = ',' + ','.join(t_re)
        return t_str in s_str
    
    def dfs(self, s, re):
        if not s:
            re.append('#')
            return
        re.append(str(s.val))
        self.dfs(s.left, re)
        self.dfs(s.right, re)
    
    