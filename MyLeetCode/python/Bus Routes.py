###
# DFS
# Time Complexity: O(n*l) n:num of routes, l: avg len of each route + O(V+E) = O(n^2) V:num of stops, E: number of edges
# Space Complexity: O(V) V:number of stops
###
class Solution(object):
    def numBusesToDestination(self, routes, S, T):
        """
        :type routes: List[List[int]]
        :type S: int
        :type T: int
        :rtype: int
        """
        stops = collections.defaultdict(set)
        for i, route in enumerate(routes):
            for s in route:
                stops[s].add(i)
        q = collections.deque([S])
        visit = set([S])
        dis = 0
        while q:
            size = len(q)
            for _ in xrange(size):
                stop = q.popleft()
                if stop == T:
                    return dis
                for route in stops[stop]:
                    for nxt in routes[route]:
                        if nxt not in visit:
                            visit.add(nxt)
                            q.append(nxt)
                    routes[route] = []
            dis += 1
        return -1
                                        
                            
                    