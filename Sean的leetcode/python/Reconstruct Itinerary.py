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
        from collections import defaultdict
        from Queue import PriorityQueue
        if not tickets:
            return []
        edges = defaultdict(PriorityQueue)
        for [s, e] in tickets:
            edges[s].put(e)
        re = []
        self.dfs("JFK", re, edges)
        return re[::-1]
    
    def dfs(self, nd, re, edges):
        while not edges[nd].empty():
            top = edges[nd].get()
            self.dfs(top, re, edges)
        re.append(nd)
            
        
        