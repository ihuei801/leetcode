###
# Union Find
# There are two cases for the tree structure to be invalid.
# 1) A node having two parents and a circle exists e.g. [[1,2],[1,3],[2,3]] => return the last one
# 2) A circle exists: [[1,2],[2,3],[3,1],[1,4]] => return the edge inside the loop 
# Approach:
# 1) Check whether there is a node having two parents. 
#     If so, store them as candidates A and B, and set the second edge invalid. 
# 2) Perform normal union find. 
#     If candidates not existing 
#            we find a circle, return current edge 
#     If the tree is now valid 
#            simply return candidate B
#     
#     else 
#            remove candidate A instead of B.
# Time Complexity: O(E)
# Space Complexity: O(V)
###
class DSU(object):
    def __init__(self, n):
        self.root = range(n)
    
    def find(self, v):
        if self.root[v] != v:
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
    def findRedundantDirectedConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if not edges:
            return []
        d = collections.defaultdict(list)
        cands = []
        for s, e in edges:
            if d[e]:
                cands.append([d[e][0], e])
                cands.append([s, e])
            d[e].append(s)
    
        n = len(edges) + 1
        dsu = DSU(n)
        for s, e in edges:
            if cands and [s, e] == cands[1]:
                continue
            if not dsu.union(s, e):
                if not cands:
                    return [s, e] #No two parents, only cycle
                break
        else:
            return cands[1] #cands[1] remove->valid
        return cands[0]
        
class Solution(object):
    def findRedundantDirectedConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        t = collections.defaultdict(list)
        cand = []
        for p, c in edges:
            if len(t[c]) != 0:
                cand.append([t[c][0], c])
                cand.append([p, c])
            t[c].append(p)
         
        root = range(len(edges) + 1)
        for p, c in edges:
            if cand and [p, c] == cand[1]:
                continue
            if not self.union(p, c, root):
                if not cand:
                    return [p, c] #No two parents, only cycle
                break
        else:
            return cand[1]    #Cand[1] remove->valid
        return cand[0]
        
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
        
                                        
                            
                    