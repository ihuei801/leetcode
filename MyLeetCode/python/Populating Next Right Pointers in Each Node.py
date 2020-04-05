###
# Time Complexity: O(n)
# Space Complexity: O(n)
###
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return None
        q = collections.deque([root])
        while q:
            pre = None
            level_size = len(q)
            for i in range(level_size):
                cur = q.popleft()
                if pre:
                    pre.next = cur
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
                pre = cur
        return root