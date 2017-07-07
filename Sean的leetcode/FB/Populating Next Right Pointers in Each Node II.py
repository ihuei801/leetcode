###
# BFS
# Time Complexity: O(n)
# Space Complexity: O(1)
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
            return
        next_level, tail = None, None
        curr = root
        while curr:
            while curr:
                if curr.left:
                    if tail:
                        tail.next = curr.left
                    else:
                        next_level = curr.left
                    tail = curr.left
                if curr.right:
                    if tail:
                        tail.next = curr.right
                    else:
                        next_level = curr.right
                    tail = curr.right
                curr = curr.next
                
            curr = next_level
            next_level, tail = None, None
            
        