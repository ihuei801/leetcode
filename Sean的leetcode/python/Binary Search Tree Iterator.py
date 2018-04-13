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
        self.stack = []
        cur = root
        while cur:
            self.stack.append(cur)
            cur = cur.left
    
        

    def hasNext(self):
        """
        :rtype: bool
        """
        
        return self.stack
            

    def next(self):
        """
        :rtype: int
        """
        tmp = self.stack.pop()
        cur = tmp.right
        while cur:
            self.stack.append(cur)
            cur = cur.left
        return tmp.val

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())