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
        