###
# BFS
# Time Complexity: O(w*l) + O(V*E) w:num of words, l:avg len of a word, V:num of unique char, E: num of edges for each char
# Space Complexity: O(V*E) 
###
class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        succ = collections.defaultdict(set)
        in_degree = collections.defaultdict(int)
        all = set(''.join(words))
        for c in all:
            in_degree[c] = 0
        for w1, w2 in zip(words, words[1:]):
            for c1, c2 in zip(w1, w2):
                if c1 != c2:
                    if c2 not in succ[c1]:
                        succ[c1].add(c2)
                        in_degree[c2] += 1
                    break
        zero_degree = collections.deque([k for k,v in in_degree.iteritems() if v == 0])
        order = ""
        while zero_degree:
            c = zero_degree.popleft()
            order += c
            for s in succ[c]:
                in_degree[s] -= 1
                if in_degree[s] == 0:
                    zero_degree.append(s)
        return order if len(order) == len(all) else ""
        