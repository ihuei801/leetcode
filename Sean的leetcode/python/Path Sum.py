###
# Time Complexity: O(n)
# Space Complexity: O(n) recursive stack
###
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, s):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        return self.dfs(root, s)

    def dfs(self, cur, s):
        if not cur:
            return False
        if not cur.left and not cur.right:
            return cur.val == s
        return self.dfs(cur.left, s - cur.val) or self.dfs(cur.right, s - cur.val)