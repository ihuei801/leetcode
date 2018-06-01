###
# Union Find
# Time Complexity: O(E) 
# Space Complexity: O(V)
###
class DSU(object):
    def __init__(self, n):
        self.root = range(n)
        
    def find(self, v1):
        if self.root[v1] != v1:
            self.root[v1] = self.find(self.root[v1])
        return self.root[v1]
    
    def union(self, v1, v2):
        r1 = self.find(v1)
        r2 = self.find(v2)
        if r1 != r2:
            self.root[r1] = r2
            return True
        return False
    
class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """    
        dsu = DSU(n)
        for v1, v2 in edges:
            if dsu.union(v1, v2):
                n -= 1
        return n











                
        
class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        if not edges:
            return n
        num = n
        root = range(n)
        for v1, v2 in edges:
            if self.union(v1, v2, root):
                num -= 1
        return num
    
    def union(self, v1, v2, root):
        r1 = self.find(v1, root)
        r2 = self.find(v2, root)
        if r1 != r2:
            root[r2] = r1
            return True
        return False
    
    def find(self, v, root):
        if v == root[v]:
            return v
        root[v] = self.find(root[v], root)
        return root[v]
        
        
        