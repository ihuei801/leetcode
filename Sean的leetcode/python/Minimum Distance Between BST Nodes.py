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
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.pre = None #need to be global because you can't pass a prev to parent
        self.re = float('inf')
        self.dfs(root)
        return self.re

    def dfs(self, cur):
        if not cur:
            return
        self.dfs(cur.left)
        if self.pre:
            self.mindist = min(self.mindist, cur.val - self.pre.val)
        self.pre = cur
        self.dfs(cur.right)