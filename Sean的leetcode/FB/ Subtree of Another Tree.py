###
# DFS
# Time Complexity: O(m+n)
# Space Complexity: O(m+n)
###
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
        s_str = ',' + self.serial(s)
        t_str = ',' + self.serial(t)
        return t_str in s_str
    def serial(self, n):
        re = []
        self.dfs(n, re)
        return ','.join(re)
    def dfs(self, n, re):
        if not n:
            re.append('#')
            return
        re.append(str(n.val))
        self.dfs(n.left, re)
        self.dfs(n.right, re)
    
    