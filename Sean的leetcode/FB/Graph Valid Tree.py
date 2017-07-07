###
# Has n-1 edges and is acyclic.
# Has n-1 edges and is connected.
# Time Complexity: O(V*E)
# Space Complexity: O(V)
###
class Solution(object):
    def find(self, v):
        return v if self.parent[v] == v else self.find(self.parent[v])
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        if len(edges) != n-1:
            return False
        self.parent = range(n)
        for e in edges:
            x, y = map(self.find, e)
            if x == y:
                return False
            self.parent[x] = y
        return True
            
            