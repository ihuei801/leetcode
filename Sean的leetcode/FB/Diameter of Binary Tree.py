###
# For every node, max path which pass it = max_depth(left subtree) + max_depth(right subtree)
# So we calculate the max_depth for a node while updating the max path for the tree
# DFS
# Time Complexity: O(n) 
# Space Complexity: O(n)
###
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        self.diamtr = 0
        self.dfs(root)
        return self.diamtr
    def dfs(self, root):
        if not root:
            return 0
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        self.diamtr = max(self.diamtr, left + right)
        return max(left, right) + 1
