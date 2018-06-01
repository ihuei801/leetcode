###
# DP
# State: dp[i]: min cost to i
# Function: dp[i] = dp[j] + A[j] for j < i
# Initialization: dp[0] = 0
# Answer: dp[n]
# Time Complexity: O(n^2)
# Space Complexity: O(n)
###
class Solution(object):
    def cheapestJump(self, A, B):
        """
        :type A: List[int]
        :type B: int
        :rtype: List[int]
        """
        if not A or A[0] == -1 or A[-1] == -1:
            return []
        n = len(A)
        dp = [float('inf')] * n
        dp[0] = 0
        l = [0] * n
        root = [-1] * n 
        for i in xrange(1, n):
            if A[i] == -1:
                continue
            for j in xrange(max(i-B, 0), i):
                if A[j] != -1:
                    cost = dp[j] + A[j]
                    if cost < dp[i] or (cost == dp[i] and l[i] < l[j] + 1):
                        dp[i] = cost
                        root[i] = j
                        l[i] = l[j] + 1
        
        re = []
        cur = n-1
        while cur >= 0:
            re.append(cur+1)
            cur = root[cur]
        
        return re[::-1] if re[-1] == 1 else []
        
                                        
                            
                    