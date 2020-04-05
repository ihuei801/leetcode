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
        self.diameter = 0
        self.dfs(root)
        return self.diameter

    def dfs(self, root):
        if not root:
            return 0
        lh = self.dfs(root.left)
        rh = self.dfs(root.right)
        self.diameter = max(self.diameter, lh + rh)
        return max(lh, rh) + 1
###
# Brute force
# Time Complexity: T(N) = N + 2T(N/2) -> O(NlogN)
# Space Complexity: O(N)
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
        return max(self.dfs(root), self.diameterOfBinaryTree(root.left),
                   self.diameterOfBinaryTree(root.right))

    def dfs(self, root):
        if not root:
            return 0
        lh = self.height(root.left)
        rh = self.height(root.right)
        return lh + rh

    def height(self, root):
        if not root:
            return 0
        return 1 + max(self.height(root.left), self.height(root.right))