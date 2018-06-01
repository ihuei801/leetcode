###
# Topological sort: https://courses.csail.mit.edu/6.006/spring11/exams/notes2-2.pdf
# BFS
# Time Complexity: O(n*w) + O(V+E) = O(alpha + n) alpha: size of alphabet = 26, n: len of word 
# Space Complexity: O(V+E) 
###
class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        if not words:
            return ""
        whole = set("".join(words))
        out_edges = collections.defaultdict(set)
        in_degree = {c: 0 for c in whole}
        for w1, w2 in zip(words, words[1:]):
            for c1, c2 in zip(w1, w2):
                if c1 != c2:
                    if c2 not in out_edges[c1]:
                        out_edges[c1].add(c2)
                        in_degree[c2] += 1
                    break
       
        q = collections.deque([c for c, v in in_degree.iteritems() if v == 0])
        re = []
        while q:
            top = q.popleft()
            re.append(top)
            for e in out_edges[top]:
                in_degree[e] -= 1
                if in_degree[e] == 0:
                    q.append(e)
            
        return "".join(re) if len(re) == len(whole) else ""

