###
# Memoize to reduce time complexity
# Think about accu = cur_sum - pre_sum
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
        return self.dfs(root, S, 0, {0: 1})

    def dfs(self, cur, S, cur_sum, pre_sum):
        if not cur:
            return 0
        cur_sum += cur.val
        if not cur.left and not cur.right:
            return pre_sum.get(cur_sum - S, 0)
        cnt = pre_sum.get(cur_sum - S, 0)
        pre_sum[cur_sum] = pre_sum.get(cur_sum, 0) + 1
        cnt += self.dfs(cur.left, S, cur_sum, pre_sum) + self.dfs(cur.right, S, cur_sum, pre_sum)
        pre_sum[cur_sum] = pre_sum.get(cur_sum) - 1
        return cnt

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