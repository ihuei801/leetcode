###
# Union Find
# Time Complexity: O(n^2*w)
# Space Complexity: O(n)
###
class Solution(object):
    def numSimilarGroups(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        if not A:
            return 0
        A = list(set(A))
        n = len(A)
        dsu = DSU(n)
        for i in xrange(n):
            for j in xrange(i + 1, n):
                if self.similar(A[i], A[j]):
                    dsu.union(i, j)
        return dsu.cnt

    def similar(self, w1, w2):
        diff = 0
        for c1, c2 in itertools.izip(w1, w2):
            if c1 != c2:
                diff += 1
            if diff > 2:
                return False
        return True


class DSU(object):
    def __init__(self, n):
        self.roots = range(n)
        self.cnt = n

    def find(self, v):
        if self.roots[v] != v:
            self.roots[v] = self.find(self.roots[v])
        return self.roots[v]

    def union(self, v1, v2):
        r1 = self.find(v1)
        r2 = self.find(v2)
        if r1 != r2:
            self.roots[r2] = r1
            self.cnt -= 1
