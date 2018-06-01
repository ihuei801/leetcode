###
# Tree
# Time Complexity: hasNext:  O(n)
# Space Complexity: O(n)
###
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
        re = [root.val]
        self.dfs1(root.left, re)
        self.dfs2(root.left, re)
        self.dfs2(root.right, re)
        self.dfs3(root.right, re)
        return re
    
    def dfs1(self, root, re):
        if not root:
            return
        if not root.left and not root.right:
            return
        re.append(root.val)
        if root.left:
            self.dfs1(root.left, re)
        else:
            self.dfs1(root.right, re)
            
    def dfs2(self, root, re):
        if not root:
            return
        if not root.left and not root.right:
            re.append(root.val)
            return
        if root.left:
            self.dfs2(root.left, re)
        if root.right:
            self.dfs2(root.right, re)
            
    def dfs3(self, root, re):
        if not root:
            return
        if not root.left and not root.right:
            return    
        if root.right:
            self.dfs3(root.right, re)
        else:
            self.dfs3(root.left, re)
        re.append(root.val)













class Solution(object):
    def boundaryOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        re = [root.val]
        
        self.add_left(root.left, re)
        self.add_leaves(root.left, re)
        self.add_leaves(root.right, re)
        self.add_right(root.right, re)
        return re 
    def add_left(self, root, re):
        if not root or (not root.left and not root.right):
            return
        re.append(root.val)
        if not root.left:
            self.add_left(root.right, re)
        else:
            self.add_left(root.left, re)
    def add_leaves(self, root, re):
        if not root:
            return
        if not root.left and not root.right:
            re.append(root.val)
            return 
        self.add_leaves(root.left, re)
        self.add_leaves(root.right, re)
    def add_right(self, root, re):
        if not root or (not root.left and not root.right):
            return
        
        if not root.right:
            self.add_right(root.left, re)
        else:
            self.add_right(root.right, re)
        re.append(root.val)
                                        
                            
                    