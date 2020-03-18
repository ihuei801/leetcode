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
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        self.maxlen = 0
        self.dfs(root)
        return self.maxlen

    def dfs(self, cur):
        if not cur:
            return 0
        lh = self.dfs(cur.left)
        rh = self.dfs(cur.right)
        l_ext = r_ext = 1  # count node, init to 1
        if cur.left and cur.left.val == cur.val + 1:
            l_ext = lh + 1
        if cur.right and cur.right.val == cur.val + 1:
            r_ext = rh + 1
        self.maxlen = max(self.maxlen, max(l_ext, r_ext))
        return max(l_ext, r_ext)

# pre-order
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        self.max_len = 0
        self.dfs(root, None, 0)
        return self.max_len
    def dfs(self, root, parent, l):
        if not root:
            return 
        if parent and parent.val + 1 == root.val:
            l += 1
        else:
            l = 1
        self.max_len = max(self.max_len, l)
        self.dfs(root.left, root, l)
        self.dfs(root.right, root, l)     

        
        