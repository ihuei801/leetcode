#######################################################################
# DFS
# Time Complexity: O(n)
# Space Complexity: O(n)  worst case not balanced
#
#
#######################################################################
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []
        re = []
        self.dfs(root, "", re)
        return re
    
    def dfs(self, root, one_sol, re):
        if not root:
            return
        if not root.left and not root.right:
            re.append(one_sol + str(root.val))
            return
        self.dfs(root.left, one_sol + str(root.val) + "->", re)  
        self.dfs(root.right, one_sol + str(root.val) + "->", re)



        
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []
        re = []
        self.dfs(root, "", re)
        return re
    def dfs(self, root, one_sol, re):
        if not root.left and not root.right:
            re.append(one_sol + str(root.val))
            return
        if root.left:
            self.dfs(root.left, one_sol + str(root.val) + "->", re)
        if root.right:
            self.dfs(root.right, one_sol + str(root.val) + "->", re)
        
        