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
        from collections import defaultdict
        d = defaultdict(dict)
        for (nu, de), v in zip(equations, values):
            d[nu][de] = v
            d[de][nu] = 1.0 / v
        re = []
        for nu, de in queries:
            ans = self.dfs(nu, de, d, set())
            if not ans:
                re.append(-1.0)
            else:
                re.append(ans)    
        return re
    
    def dfs(self, nu, de, d, visit):
        if nu in visit:
            return None
        if nu not in d or de not in d:
            return None
        if nu == de:
            return 1.0
        if de in d[nu]:
            return d[nu][de]
        visit.add(nu)
        for e in d[nu].keys():
            res = self.dfs(e, de, d, visit)
            if res:
                return res * d[nu][e]
        visit.remove(nu)
        return None
        
        