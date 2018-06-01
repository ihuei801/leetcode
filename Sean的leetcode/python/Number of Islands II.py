###
# Union Find
# Time Complexity: O(k) 
# Space Complexity: O(m*n)
###
class DSU(object):
    def __init__(self, n):
        self.root = [-1] * n
        
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
    def numIslands2(self, m, n, positions):
        """
        :type m: int
        :type n: int
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        if not positions:
            return []
        dsu = DSU(m*n)
        num = 0
        re = []
        for i, j in positions:
            idx = i * n + j
            if dsu.root[idx] == -1:
                num += 1
                dsu.root[idx] = idx
                for nbi, nbj in ((i+1, j), (i-1, j), (i, j+1), (i, j-1)):
                    nbidx = nbi * n + nbj
                    if nbi >= 0 and nbi < m and nbj >= 0 and nbj < n and dsu.root[nbidx] != -1 and dsu.union(idx, nbidx):
                        num -= 1
            re.append(num)
        return re
        
        

        
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
        
        
        