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
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        if not root:
            return []
        q = collections.deque([root])
        result = []
        while q:
            level_size = len(q)
            level_sum = 0.0
            for i in xrange(level_size):
                cur = q.popleft()
                level_sum += cur.val
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            result.append(level_sum/level_size)
        return result