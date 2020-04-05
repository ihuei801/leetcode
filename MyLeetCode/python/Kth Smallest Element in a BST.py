###
# we need a global cnt to count the number of node we have visit rather than substract
# k because k is a copy to every function call
# Time Complexity: O(k)
# Space Complexity: O(h)
###
# Recursive
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.cnt = 0
        self.re = None
        self.dfs(root, k)
        return self.re

    def dfs(self, root, k):
        if not root:
            return
        self.dfs(root.left, k)
        self.cnt += 1
        if self.cnt == k:
            self.re = root.val
            return
        self.dfs(root.right, k)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        if not k or not root:
            return -1
        stk = []
        cnt = 0
        cur = root
        while cur:
            stk.append(cur)
            cur = cur.left
        while stk:
            top = stk.pop()
            cnt += 1
            if cnt == k:
                return top.val
            cur = top.right
            while cur:
                stk.append(cur)
                cur = cur.left
        return -1
        
