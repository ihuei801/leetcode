###
# Tree
# Time Complexity: O(n)
# Space Complexity: O(1) ignore recursive
###
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        self.pre = None
        self.maxcnt = 0
        self.curcnt = 0
        self.re = []
        self.dfs(root)
        return self.re
    
    def dfs(self, root):
        if not root:
            return
        self.dfs(root.left)
        if self.pre and self.pre.val == root.val:
            self.curcnt += 1
        else:
            self.curcnt = 1
        if self.curcnt == self.maxcnt:
            self.re.append(root.val)
        elif self.curcnt > self.maxcnt:
            self.re = [root.val]           #assign a list in a function, need to do re[:] = [root.val]
            self.maxcnt = self.curcnt 
        self.pre = root
        self.dfs(root.right)
    

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.max_cnt = 0
        self.cur_cnt = 0
        self.prev = None
        self.fill = False
        self.dfs(root)
        self.re = []
        self.prev = None
        self.cur_cnt = 0
        self.fill = True
        self.dfs(root)
        return self.re
        
    def dfs(self, root):
        if not root:
            return
        self.dfs(root.left)
        if self.prev and self.prev.val == root.val:
            self.cur_cnt += 1         
        else:
            self.cur_cnt = 1
        if not self.fill:
            self.max_cnt = max(self.max_cnt, self.cur_cnt)
        else:
            if self.cur_cnt == self.max_cnt:
                self.re.append(root.val)
        self.prev = root
        self.dfs(root.right)
        
        
                                        
                            
                    