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
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.max_sum = -float('inf')
        self.dfs(root)
        return self.max_sum

    def dfs(self, root):
        if not root:
            return 0
        lsum = max(self.dfs(root.left), 0)
        rsum = max(self.dfs(root.right), 0)
        self.max_sum = max(self.max_sum, root.val + lsum + rsum)
        return max(lsum, rsum) + root.val
                            
                    