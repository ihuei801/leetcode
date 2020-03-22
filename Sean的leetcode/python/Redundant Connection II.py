###
# Union Find
# There are two cases for the tree structure to be invalid.
# 1) A node having two parents and a circle exists e.g. [[1,2],[1,3],[2,3]] => return the last one
# 2) Only a circle exists: [[1,2],[2,3],[3,1],[1,4]] => return the edge inside the loop
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
class Solution(object):
    def findRedundantDirectedConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if not edges:
            return []
        ins, cands = self.build_ins_and_cands(edges)
        n = len(edges) + 1
        dsu = DSU(n)
        result = []
        for v1, v2 in edges:
            if cands and cands[1] == [v1, v2]:
                continue
            if not dsu.union(v1, v2):
                if not cands:
                    return [v1, v2]
                return cands[0] # Even cands[1] remove still invalid, should remove cands[0]
        return cands[1]

    def build_ins_and_cands(self, edges):
        ins = collections.defaultdict(list)
        cands = []
        for v1, v2 in edges:
            if ins[v2]:
                cands.append([ins[v2][0], v2])
                cands.append([v1, v2])
            ins[v2].append(v1)
        return ins, cands


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
        
                                        
                            
                    