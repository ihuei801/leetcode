###
# Has n-1 edges and is acyclic.
# Has n-1 edges and is connected.
# Compressed_find => find: O(1)
# Time Complexity: O(E)
# Space Complexity: O(V)
###
class DSU(object):
    def __init__(self, num):
        self.root = range(num)
        
    def find(self, e):
        if self.root[e] != e:
            self.root[e] = self.find(self.root[e])
        return self.root[e]
    
    def union(self, e1, e2):
        r1 = self.find(e1)
        r2 = self.find(e2)
        if r1 != r2:
            self.root[r1] = r2
            return True
        return False
        
class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        if len(edges) != n-1:
            return False
        dsu = DSU(n)
        for v1, v2 in edges:
            if not dsu.union(v1, v2):
                return False
        return True
    
            

class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        if len(edges) != n-1:
            return False
        root = range(n)
        for v1, v2 in edges:
            if not self.union(v1, v2, root):
                return False
        return True
    
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
        root[v] = self.find(root[v], root) #compressed find
        return root[v]
            
        
            
        
            
        