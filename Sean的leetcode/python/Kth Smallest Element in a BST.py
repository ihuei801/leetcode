###
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
        stack = []
        cur = root
        i = 0
        while cur:
            stack.append(cur)
            cur = cur.left
        while self.stack:
            tmp = stack.pop()
            i += 1
            if i == k:
                return tmp.val
            cur = tmp.right
            while cur:
                stack.append(cur)
                cur = cur.left
        return -1        


                       
        