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
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        result = []
        q = collections.deque([root])
        isLToR = True
        while q:
            level_size = len(q)
            level_node = deque()
            for i in xrange(level_size):
                cur = q.popleft()
                if isLToR:
                    level_node.append(cur.val)
                else:
                    level_node.appendleft(cur.val)
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            result.append(level_node)
            isLToR = not isLToR
        return result