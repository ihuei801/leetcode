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
        self.max_path = 0
        self.maxDepth(root)
        return self.max_path
    def maxDepth(self, root):
        if not root:
            return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        self.max_path = max(self.max_path, left + right)
        return max(left, right) + 1