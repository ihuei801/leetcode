###
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
    def splitBST(self, root, V):
        """
        :type root: TreeNode
        :type V: int
        :rtype: List[TreeNode]
        """
        if not root:
            return [None, None]
        if root.val <= V: # the root is always on the left, we want to split the right subtree
            st, bt = self.splitBST(root.right, V)
            root.right = st
            return [root, bt]
        else: # the root is always on the right, we want to split the left subtree
            st, bt = self.splitBST(root.left, V)
            root.left = bt
            return [st, root]
