###
# BFS
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
###
# Follow up: constant space
# Time Complexity: O(n)
# Space Complexity: O(1)
###
###
# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None
class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if not root:
            return None
        next_h = pre = None
        cur = root
        while cur:
            if cur.left:
                if not next_h:
                    next_h = cur.left
                else:
                    pre.next = cur.left
                pre = cur.left
            if cur.right:
                if not next_h:
                    next_h = cur.right
                else:
                    pre.next = cur.right
                pre = cur.right
            if cur.next:
                cur = cur.next
            else:
                cur = next_h
                next_h = pre = None

