###
# DSU: Disjoint set union
# Has n-1 edges and is acyclic.
# Has n-1 edges and is connected.
# Compressed_find => find: O(1)
# Time Complexity: O(E)
# Space Complexity: O(V)
###
class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        if len(edges) != n - 1:
            return False
        dsu = DSU(n)
        for v1, v2 in edges:
            if not dsu.union(v1, v2):
                return False
        return True


class DSU(object):
    def __init__(self, n):
        self.roots = range(n)

    def find(self, v):
        if self.roots[v] != v:
            self.roots[v] = self.find(self.roots[v])  # compressed find
        return self.roots[v]

    def union(self, v1, v2):
        r1 = self.find(v1)
        r2 = self.find(v2)
        if r1 != r2:
            self.roots[r2] = r1
            return True
        return False


class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        # Condition 1: The graph must contain n - 1 edges
        if len(edges) != n - 1:
            return False
        # Condition 2: The graph must contain a single connected component
        dsu = DSU(n)
        for v1, v2 in edges:
            if not dsu.union(v1, v2):
                return False
        return True


class DSU(object):
    def __init__(self, n):
        self.roots = range(n)

    def find(self, v):
        while self.roots[v] != v:
            v = self.roots[v]
        return v

    def union(self, v1, v2):
        r1 = self.find(v1)
        r2 = self.find(v2)
        if r1 != r2:
            self.roots[r2] = r1
            return True
        return False



            
        
            
        