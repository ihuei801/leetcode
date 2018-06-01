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
###
class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        if not tickets:
            return []
        edges = collections.defaultdict(list)
        for s, e in tickets:
            heapq.heappush(edges[s], e)
        re = []
        self.dfs("JFK", edges, re)
        return re[::-1]
    
    def dfs(self, start, edges, re):
        while edges[start]:
            nxt = heapq.heappop(edges[start])
            self.dfs(nxt, edges, re)
        re.append(start)
        
            
        


            
        
        