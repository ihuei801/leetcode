###
# Time Complexity: hasNext: O(1) next: Amortized(in average) O(1) visit each node once
# Space Complexity: O(h)
###

# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stk = []
        cur = root
        while cur:
            self.stk.append(cur)
            cur = cur.left

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.stk) != 0

    def next(self):
        """
        :rtype: int
        """
        top = self.stk.pop()
        cur = top.right
        while cur:
            self.stk.append(cur)
            cur = cur.left
        return top.val

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())