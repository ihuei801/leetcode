###
# Tree DFS Serialization
# Time Complexity: O(n^2) n nodes and build string O(n)
# Space Complexity: O(n^2)
###
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        d = collections.Counter()
        re = []
        self.dfs(root, d, re)
        return re
    
    def dfs(self, root, d, re):
        if not root:
            return "#"
        key = str(root.val) + "," + self.dfs(root.left, d, re) + "," + self.dfs(root.right, d, re)
        if d[key] == 1:
            re.append(root)
        d[key] += 1
        return key
        
            
        
            
                                        
                            
                    