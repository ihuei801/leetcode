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
        result = []
        while q:
            level_size = len(q)
            level_node = []
            for i in xrange(level_size):
                cur = q.popleft()
                level_node.append(cur.val)
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            result.append(level_node)
        return result

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
        result = []
        while q:
            next_q = []
            level = []
            for cur in q:
                level.append(cur.val)
                if cur.left:
                    next_q.append(cur.left)
                if cur.right:
                    next_q.append(cur.right)
            result.append(level)
            q = next_q
        return result
