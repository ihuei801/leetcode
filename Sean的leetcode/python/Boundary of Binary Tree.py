# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def boundaryOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        result = [root.val]
        self.lb(root.left, result)
        self.leave(root.left, result)
        self.leave(root.right, result)
        self.rb(root.right, result)
        return result

    def lb(self, cur, result):
        if not cur:
            return
        if not cur.left and not cur.right:
            return
        result.append(cur.val)
        if cur.left:
            self.lb(cur.left, result)
        else:
            self.lb(cur.right, result)

    def leave(self, cur, result):
        if not cur:
            return
        if not cur.left and not cur.right:
            result.append(cur.val)
        self.leave(cur.left, result)
        self.leave(cur.right, result)

    def rb(self, cur, result):
        if not cur:
            return
        if not cur.left and not cur.right:
            return
        if cur.right:
            self.rb(cur.right, result)
        else:
            self.rb(cur.left, result)
        result.append(cur.val)
