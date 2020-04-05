###
# BFS
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
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        q = collections.deque([root])
        re = []
        while q:
            n = len(q)
            level = []
            for i in xrange(n):
                e = q.popleft()
                level.append(e.val)
                if e.left:
                    q.append(e.left)
                if e.right:
                    q.append(e.right)
            re.append(level)
        return re

# Solution 2
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        q = [root]
        re = []
        while q:
            next_q = []
            level = []
            for n in q:
                level.append(n.val)
                if n.left:
                    next_q.append(n.left)
                if n.right:
                    next_q.append(n.right)
            re.append(level)
            q = next_q
        return re
        