###
# Sliding Window
# Time Complexity: O(n)
# Space Complexity: O(1)
###
class Solution(object):
    def longestOnes(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        l = 0
        maxlen = 0
        onecnt = 0
        for r, e in enumerate(A):
            if e == 1:
                onecnt += 1
            while r - l + 1 - onecnt > K:
                if A[l] == 1:
                    onecnt -= 1
                l += 1
            maxlen = max(maxlen, r - l + 1)
        return maxlen