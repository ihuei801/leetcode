###
# DFS
# Use two traversals on the tree, we can root at any node.
# (0) Initial an array count, count[i] counts all nodes in the subtree i.
#     Initial an array of sumdis, sumdis[i] counts sum of distance in subtree i.
# (1) Post-Order: Calculate the size of each subtree and the sum distance from the root to each subtree. 
#                 The sum distance for our chosen root is the correct sum distance for the entire tree.
# (2) Pre-Order: Calculte the sum distance in the whole tree for each node, using the size of each subtree. 
#                The child gets closer to part of the nodes than its parent and gets further from part of the nodes than its parent
# Time Complexity: O(n)
# Space Complexity: O(n)
###
class Solution(object):
    def sumOfDistancesInTree(self, N, edges):
        """
        :type N: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        d = collections.defaultdict(set)
        for e1, e2 in edges:
            d[e1].add(e2)
            d[e2].add(e1)
        sumdis = [0] * N
        cnt = [0] * N
        self.dfs(0, d, sumdis, cnt, set())
        self.dfs2(0, d, sumdis, cnt, set(), N)
        return sumdis
    
    def dfs(self, root, d, sumdis, cnt, visit):
        visit.add(root)
        for sub in d[root]:
            if sub not in visit:
                self.dfs(sub, d, sumdis, cnt, visit)
                cnt[root] += cnt[sub]
                sumdis[root] += sumdis[sub] + cnt[sub]
        cnt[root] += 1
        
    def dfs2(self, root, d, sumdis, cnt, visit, N): 
        visit.add(root)
        for sub in d[root]:
            if sub not in visit:
                sumdis[sub] = sumdis[root] - cnt[sub] + (N- cnt[sub])
                self.dfs2(sub, d, sumdis, cnt, visit, N)
        
    


        
class Solution(object):
    def sumOfDistancesInTree(self, N, edges):
        """
        :type N: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        d = collections.defaultdict(set)
        for e1, e2 in edges:
            d[e1].add(e2)
            d[e2].add(e1)
        cnt = [0] * N
        sumdis = [0] * N
        
        def dfs(root, visit):
            visit.add(root)
            for sub in d[root]:
                if sub not in visit:
                    dfs(sub, visit)
                    cnt[root] += cnt[sub]
                    sumdis[root] += sumdis[sub] + cnt[sub]
            cnt[root] += 1
            
        def dfs2(root, visit):
            visit.add(root)
            for sub in d[root]:
                if sub not in visit:
                    sumdis[sub] = sumdis[root] - cnt[sub] + (N - cnt[sub])
                    dfs2(sub, visit)
                    
        dfs(0, set())
        dfs2(0, set())
        return sumdis
    
        
    
        
                                        
                            
                    