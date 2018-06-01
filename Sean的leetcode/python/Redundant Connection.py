###
# Union Find 
# Time Complexity: O(E)
# Space Complexity: O(V)
###
class DSU(object):
    def __init__(self, n):
        self.root = range(n)
        
    def find(self, v):
        if v != self.root[v]:
            self.root[v] = self.find(self.root[v])
        return self.root[v]
    
    def union(self, v1, v2):
        r1 = self.find(v1)
        r2 = self.find(v2)
        if r1 != r2:
            self.root[r1] = r2
            return True
        return False
    
class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if not edges:
            return []
        n = len(edges)+1
        dsu = DSU(n)
        for v1, v2 in edges:
            if not dsu.union(v1, v2):
                return [v1, v2]
        
                     
   
class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        root = range(len(edges)+1)
        for e1, e2 in edges:
            if not self.union(e1, e2, root):
                return [e1, e2]
                     
    def union(self, e1, e2, root):
        r1 = self.find(e1, root)
        r2 = self.find(e2, root)
        if r1 != r2:
            root[r1] = r2
            return True
        return False
    
    def find(self, e, root):
        if root[e] == e:
            return e
        root[e] = self.find(root[e], root)
        return root[e]
            
                                        
                            
                    