###
# BFS: ensure that upper level is printed before lower level
# Time Complexity: O(nlogn) (sorted dict)
# Space Complexity: O(n)
###
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        q = [(root, 0)]
        table = collections.defaultdict(list)
        for node, i in q:
            table[i].append(node.val)
            if node.left:
                q.append((node.left, i-1))
            if node.right:
                q.append((node.right, i+1))
        return [table[i] for i in sorted(table)]