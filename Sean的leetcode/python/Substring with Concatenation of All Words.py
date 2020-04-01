###
# Sliding Window - Fixed size
# Time Complexity: O(N*M*L) L: len of a word
# Space Complexity: O(N+M) N:len of s, M:num of words
###
class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not s or not words:
            return []
        d = collections.Counter(words)
        w_len = len(words[0])
        w_cnt = len(words)
        result = []
        for l in xrange(len(s) - w_len * w_cnt + 1):
            word_seen = collections.Counter()
            for i in xrange(w_cnt):
                word_l = l + i * w_len
                word = s[word_l : word_l + w_len]
                if word not in d:
                    break
                word_seen[word] += 1
                if word_seen[word] > d[word]:
                    break
                if i + 1 == w_cnt:
                    result.append(l)
        return result


                