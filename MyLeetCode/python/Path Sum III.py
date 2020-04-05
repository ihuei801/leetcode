###
# Memoize to reduce time complexity
# Think about accu = cur_sum - pre_sum
# use a global count to store the number of path that sums to S
# Time Complexity: O(N)
# Space Complexity: O(N)
###
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, S):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        self.cnt = 0
        self.dfs(root, S, 0, {0: 1})
        return self.cnt

    def dfs(self, cur, S, cur_sum, pre_sum):
        if not cur:
            return
        cur_sum += cur.val
        if not cur.left and not cur.right:
            self.cnt += pre_sum.get(cur_sum - S, 0)
            return
        self.cnt += pre_sum.get(cur_sum - S, 0)
        pre_sum[cur_sum] = pre_sum.get(cur_sum, 0) + 1
        self.dfs(cur.left, S, cur_sum, pre_sum)
        self.dfs(cur.right, S, cur_sum, pre_sum)
        pre_sum[cur_sum] = pre_sum.get(cur_sum) - 1
        return

    ###
# Brute force
# Time Complexity: T(N) = N + 2T(N/2) -> O(NlogN)
# Space Complexity: O(N)
###
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, S):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if root:
            return self.dfs(root, S) + self.pathSum(root.left, S) + self.pathSum(root.right, S) # Treat it as a root-to-leaf problem for subtrees
        return 0

    def dfs(self, cur, S):
        if not cur:
             return 0
        if not cur.left and not cur.right:
             return int(cur.val == S)
        return int(S == cur.val) + self.dfs(cur.left, S-cur.val) + self.dfs(cur.right, S-cur.val)