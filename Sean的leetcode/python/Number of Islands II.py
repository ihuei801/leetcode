###
# Union Find
# Time Complexity: O(k) 
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
        
        
        