###
# DFS
# Time Complexity: O(nlogn) n:row m:col k:len of word
# Space Complexity: O(n)
###
class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        if len(envelopes) <= 1:
            return len(envelopes)
        envelopes.sort(key = lambda x: (x[0], -x[1]))
        dp = []
        for i, e in enumerate(envelopes):
            it = bisect.bisect_left(dp, e[1])
            if it < len(dp):
                dp[it] = e[1]
            else:
                dp.append(e[1])
        return len(dp)
            