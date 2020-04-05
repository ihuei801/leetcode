###
# Time Complexity: O(n) traverse n node
# Space Complexity: O(n) recursive stack
###
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.dfs(root, 0)

    def dfs(self, cur, one_sol):
        if not cur:
            return 0
        if not cur.left and not cur.right:
            return one_sol * 10 + cur.val
        return self.dfs(cur.left, one_sol * 10 + cur.val) + self.dfs(cur.right, one_sol * 10 + cur.val)