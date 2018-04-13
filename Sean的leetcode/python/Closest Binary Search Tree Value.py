###
# Tree Search
# Time Complexity: O(h)
###
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        if not root:
            return -float('inf')
        close = root.val
        cur = root
        while cur:
            if target == cur.val:
                return cur.val    
            if abs(target - cur.val) < abs(target-close):
                close = cur.val
            if cur.val > target:
                cur = cur.left
            else:
                cur = cur.right
        return close
                      
                            
                    