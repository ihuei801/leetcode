###
# BFS
# Time Complexity: O(n)
# Space Complexity: O(logn)
###
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        from collections import deque
        if not root:
            return 0
        sum = 0
        q = deque([root])
        while q:
            tmp = q.popleft()
            if tmp.left:
                if not tmp.left.left and not tmp.left.right:
                    sum += tmp.left.val
                q.append(tmp.left)
            if tmp.right:
                q.append(tmp.right)
        return sum
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
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        sum = 0
        if root.left:
            if not root.left.left and not root.left.right:
                sum += root.left.val
            else:
                sum += self.sumOfLeftLeaves(root.left)
            
        if root.right: 
            sum += self.sumOfLeftLeaves(root.right)
        return sum