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
        self.push_all(root)

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.stack
        

    def next(self):
        """
        :rtype: int
        """
        node = self.stack.pop()
        self.push_all(node.right)
        return node.val
        
    def push_all(self, root):
        while root:
            self.stack.append(root)
            root = root.left

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())