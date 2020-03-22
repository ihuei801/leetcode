###
# Graph
# Eulerian path: a trail in a finite graph which visits every edge exactly once => 
# zero or two vertices have an odd degree 
# If there are exactly two vertices of odd degree, all Eulerian trails start at one of them and end at the othe
# Eulerian cycle: an Eulerian path which starts and ends on the same vertex. => no vertices of odd degree
# Euler Circuit in a Directed Graph
# https://www.geeksforgeeks.org/euler-circuit-directed-graph/
# Hierholzer’s Algorithm for directed graph
# https://www.geeksforgeeks.org/hierholzers-algorithm-directed-graph/
# Time Complexity: O(ElogE) (create edge) + O(E) (dfs visit each edge once) + O(E) reverse
# Space Complexity: Graph(O(V) + O(E)) + O(E)
###
class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        if not tickets:
            return []
        outs = self.build_outs(tickets)
        result = []
        self.dfs("JFK", outs, result)
        return result[::-1]

    def build_outs(self, tickets):
        outs = collections.defaultdict(list)
        for s, e in tickets:
            heapq.heappush(outs[s], e)
        return outs

    def dfs(self, start, outs, result):
        while outs[start]:
            nxt = heapq.heappop(outs[start])
            self.dfs(nxt, outs, result)
        result.append(start)
        
            
        


            
        
        