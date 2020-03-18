###
# Time Complexity: O(nlogn) traverse n node, each node make copy of current path
# Space Complexity: O(nlogn) recursive stack
###
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, s):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        result = []
        self.dfs(root, s, [], result)
        return result

    def dfs(self, cur, s, one_sol, result):
        if not cur:
            return
        if not cur.left and not cur.right:
            if cur.val == s:
                result.append(one_sol + [cur.val])
            return

        self.dfs(cur.left, s - cur.val, one_sol + [cur.val], result)
        self.dfs(cur.right, s - cur.val, one_sol + [cur.val], result)