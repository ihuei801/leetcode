###
# Tree
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
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.maxlen = 0
        self.dfs(root, None)
        return self.maxlen

    def dfs(self, cur, parent):
        if not cur:
            return 0
        lh = self.dfs(cur.left, cur)
        rh = self.dfs(cur.right, cur)
        l_ext = r_ext = 0
        if cur.left and cur.left.val == cur.val:
            l_ext = lh + 1
        if cur.right and cur.right.val == cur.val:
            r_ext = rh + 1
        self.maxlen = max(self.maxlen, l_ext + r_ext)
        return max(l_ext, r_ext)
        
        