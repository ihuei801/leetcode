###
# Union Find
# Time Complexity: O(m*n+k)  m*n to initialize union find, k to process
# Space Complexity: O(m*n)
###
class Solution(object):
    def numIslands2(self, m, n, positions):
        """
        :type m: int
        :type n: int
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        if not m or not n or not positions:
            return []
        dsu = DSU(m * n)
        result = []
        for i, j in positions:
            idx = i * n + j
            if dsu.roots[idx] == -1:
                dsu.roots[idx] = idx
                dsu.cnt += 1
                self.union_around(i, j, m, n, dsu)
            result.append(dsu.cnt)
        return result

    def union_around(self, i, j, m, n, dsu):
        idx = i * n + j
        for nbi, nbj in ((i - 1, j), (i + 1, j), (i, j + 1), (i, j - 1)):
            if nbi >= 0 and nbi < m and nbj >= 0 and nbj < n:
                nb_idx = nbi * n + nbj
                if dsu.roots[nb_idx] != -1:
                    dsu.union(idx, nb_idx)


class DSU(object):
    def __init__(self, n):
        self.roots = [-1] * n
        self.cnt = 0

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
            return True
        return False
        
        

        
class Solution(object):
    def numIslands2(self, m, n, positions):
        """
        :type m: int
        :type n: int
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        if not positions:
            return []
        root = [-1] * (m * n)
        num = 0
        direc = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        re = []
        for i, j in positions:
            idx = i*n+j
            if root[idx] == -1:
                num += 1
                root[idx] = idx
                for di, dj in direc:
                    nbi = i + di
                    nbj = j + dj
                    nbidx = nbi * n + nbj
                    if nbi >= 0 and nbi < m and nbj >= 0 and nbj < n and root[nbidx] != -1:
                        if self.union(idx, nbidx, root):
                            num -= 1
            re.append(num)
        return re
    
    def union(self, v1, v2, root):
        r1 = self.find(v1, root)
        r2 = self.find(v2, root)
        if r1 != r2:
            root[r2] = r1
            return True
        return False
        
    def find(self, v, root):
        if root[v] == v:
            return v
        root[v] = self.find(root[v], root)
        return root[v]
        
        
        