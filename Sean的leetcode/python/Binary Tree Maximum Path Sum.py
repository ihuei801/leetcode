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
        self.maxsum = -float('inf')
        self.dfs(root)
        return self.maxsum
    def dfs(self, root):
        if not root:
            return 0
        left_sum = self.dfs(root.left)
        right_sum = self.dfs(root.right)
        l_sum, r_sum = root.val, root.val
        if left_sum > 0:
            l_sum += left_sum
        if right_sum > 0:
            r_sum += right_sum
        self.maxsum = max(self.maxsum, l_sum + r_sum - root.val)
        return max(l_sum, r_sum) 
                                        
                            
                    