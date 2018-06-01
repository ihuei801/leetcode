###
# BFS Topological sort
# Time Complexity: O(n*l) + O(V+E)
# Space Complexity: O(V+E)
###
class Solution(object):
    def sequenceReconstruction(self, org, seqs):
        """
        :type org: List[int]
        :type seqs: List[List[int]]
        :rtype: bool
        """
        if not org or not seqs:
            return False
        whole = set([e for seq in seqs for e in seq])
        if len(org) != len(whole):
            return False
        in_degree = {c: 0 for c in whole}
        out_edges = collections.defaultdict(set)
        for seq in seqs:
            for s, e in zip(seq, seq[1:]):
                if e not in out_edges[s]:
                    out_edges[s].add(e)
                    in_degree[e] += 1
        q = [key for key, value in in_degree.iteritems() if value == 0]
        idx = 0
        while q:
            if len(q) != 1:
                return False
            top = q.pop()
            if top != org[idx]:
                return False
            idx += 1
            for e in out_edges[top]:
                in_degree[e] -= 1
                if in_degree[e] == 0:
                    q.append(e)
        return idx == len(org)
            
            
            
            
            
                
        
        