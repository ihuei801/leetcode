###
# Union Find
# Compressed_find => find: O(1)
# Time Complexity: O(E)
# Space Complexity: O(V)
###
class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if not edges:
            return []
        n = len(edges) + 1
        dsu = DSU(n)
        for v1, v2 in edges:
            if not dsu.union(v1, v2):
                return [v1, v2]
        return []


class DSU(object):
    def __init__(self, n):
        self.roots = range(n)

    def find(self, v):
        if self.roots[v] != v:
            self.roots[v] = self.find(self.roots[v])
        return self.roots[v]

    def union(self, v1, v2):
        r1 = self.find(v1)
        r2 = self.find(v2)
        if r1 != r2:
            self.roots[r2] = r1
            return True
        return False
        
                     
   
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
            
                                        
                            
                    