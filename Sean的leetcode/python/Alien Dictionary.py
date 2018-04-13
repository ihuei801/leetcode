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
        succ = collections.defaultdict(set)
        whole = set(''.join(words))
        in_degree = {k: 0 for k in whole}
        for c in whole:
            in_degree[c] = 0
        for w1, w2 in zip(words, words[1:]):
            for c1, c2 in zip(w1, w2):
                if c1 != c2:
                    if c2 not in succ[c1]:
                        succ[c1].add(c2)
                        in_degree[c2] += 1
                    break
        q = [k for k, v in in_degree.iteritems() if v == 0]
        re = ""
        while q:
            next_q = []
            for e in q:
                re += e
                for s in succ[e]:
                    in_degree[s] -= 1
                    if in_degree[s] == 0:
                        next_q.append(s)
            q = next_q
        return re if len(re) == len(whole) else ""

