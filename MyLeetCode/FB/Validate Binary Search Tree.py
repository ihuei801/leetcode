###
# BST
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
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        self.stack = []
        self.push_all(root)
        pre = None
        while self.stack:
            n = self.stack.pop()
            if pre and pre.val >= n.val:
                return False
            pre = n
            self.push_all(n.right)
        return True
        
    def push_all(self, root):
        while root:
            self.stack.append(root)
            root = root.left