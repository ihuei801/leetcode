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
            
        