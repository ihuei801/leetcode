###
# BFS
# Time Complexity: O(n) 
# Space Complexity: O(n)
###
class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if n <= 2:
            return range(n)
        d = collections.defaultdict(set)
        for e1, e2 in edges:
            d[e1].add(e2)
            d[e2].add(e1)
        
        q = collections.deque([k for k, v in d.iteritems() if len(v) == 1])
        num = n
        while num > 2:
            size = len(q)
            num -= size
            for _ in xrange(size):
                top = q.popleft()
                for nxt in d[top]:
                    if top in d[nxt]:
                        d[nxt].remove(top)
                        if len(d[nxt]) == 1:
                            q.append(nxt)
        return list(q)







        
class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if not n:
            return []
        if n == 1:
            return [0]
        table = collections.defaultdict(set)
        for edge in edges:
            table[edge[0]].add(edge[1])
            table[edge[1]].add(edge[0])
        q = [k for k, v in table.iteritems() if len(v) == 1]
        num = n
        while num > 2:
            next_q = []
            num -= len(q)
            for nd in q:
                nb = table[nd].pop()
                table[nb].remove(nd)
                if len(table[nb]) == 1:
                    next_q.append(nb)
            q = next_q
        return q 
        