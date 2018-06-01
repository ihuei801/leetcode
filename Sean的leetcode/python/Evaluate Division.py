###
# Graph
# DFS
# Time Complexity: O(E) (build a graph) + O(Q*E) 
###
class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        edges = collections.defaultdict(dict)
        for (nu, de), v in zip(equations, values):
            edges[nu][de] = v
            edges[de][nu] = 1 / v
        re = []
        for nu, de in queries:
            ans = self.dfs(edges, nu, de, set())
            if ans:
                re.append(ans)
            else:
                re.append(-1.0)
        return re
    
    def dfs(self, edges, nu, de, visit):
        if nu not in edges or de not in edges:
            return None
        if nu == de:
            return 1.0
        if de in edges[nu]:
            return edges[nu][de]
        visit.add(nu)
        for nxt, v in edges[nu].iteritems():
            if nxt not in visit:
                ans = self.dfs(edges, nxt, de, visit)
                if ans:
                    return v * ans
        visit.remove(nu)
        return None
                
                
class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        edges = collections.defaultdict(dict)
        for (nu, de), v in zip(equations, values):
            edges[nu][de] = v
            edges[de][nu] = 1 / v
        re = []
        for nu, de in queries:
            ans = self.dfs(edges, nu, de, set())
            if ans:
                re.append(ans)
            else:
                re.append(-1.0)
        return re
    
    def dfs(self, edges, nu, de, visit):
        if nu not in edges or de not in edges:
            return None
        if nu in visit:
            return None
        if nu == de:
            return 1.0
        if de in edges[nu]:
            return edges[nu][de]
        visit.add(nu)
        for nxt, v in edges[nu].iteritems():
            ans = self.dfs(edges, nxt, de, visit)
            if ans:
                return v * ans
        visit.remove(nu)
        return None
                
        
        