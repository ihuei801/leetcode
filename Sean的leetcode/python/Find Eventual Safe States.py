###
# Graph
# Time Complexity: O(V+E)
# Space Complexity: O(V)
###
class Solution(object):
    def eventualSafeNodes(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """
        if not graph:
            return []
        out_edges = map(set, graph)
        in_edges = [set() for i in xrange(len(out_edges))] #can't do [set()] * n because it refers to the same set object
        q = collections.deque()
        for i, edges in enumerate(out_edges):
            if not edges:
                q.append(i)
            else:
                for e in edges:
                    in_edges[e].add(i)
        safe = [False] * len(out_edges)
        while q:
            top = q.popleft()
            safe[top] = True
            for s in in_edges[top]:
                out_edges[s].remove(top)
                if not out_edges[s]:
                    q.append(s)
        return [i for i, v in enumerate(safe) if v]

                    
                            
                    