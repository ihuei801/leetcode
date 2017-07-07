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
        s_serial = ',' + self.serialize(s)
        t_serial = ',' + self.serialize(t)
        return t_serial in s_serial 
    def serialize(self, s):
        re = []
        self.serial(s, re)
        return ','.join(re)
    def serial(self, s, re):
        if not s:
            re.append('#')
            return
        re.append(str(s.val))
        self.serial(s.left, re)
        self.serial(s.right, re)
    