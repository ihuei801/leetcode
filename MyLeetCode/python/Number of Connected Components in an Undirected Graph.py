###
# Union Find
# Time Complexity: O(E) 
# Space Complexity: O(V)
###
class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        if not edges:
            return n
        dsu = DSU(n)
        result = n
        for v1, v2 in edges:
            if dsu.union(v1, v2):
                result -= 1
        return result


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
        
        
        