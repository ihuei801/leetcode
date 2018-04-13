###
# Time Complexity: O(k)
# Space Complexity: O(h)
###
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
        self.count = 0
        self.result = 0
        self.inorder(root, k)
        return self.result
    
    def inorder(self, root, k):
        if not root:
            return 
        self.inorder(root.left, k)
        self.count += 1
        if self.count == k:
            self.result = root.val
        self.inorder(root.right, k)
                       
        