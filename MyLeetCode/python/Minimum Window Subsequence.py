###
# DP
# State: dp[i][j]: start index that first i chars in S contains a subseq of first j chars in T
# Function: dp[i][j] = dp[i-1][j-1] if S[i] == T[j]
#           dp[i][j] = dp[i-1][j] if S[i] != T[j]
# Initialization: dp[i][0] = i if S[i] == T[0] 
#                 dp[i][0] = dp[i-1][0] if S[i] != T[0]
# Answer: i - dp[i][n-1] +1 for i in [0, m] if dp[i][n-1]!= -1
# Time Complexity: O(mn)
# Space Complexity: O(n)
###
class Solution(object):
    def minWindow(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        m = len(S)
        n = len(T)
        dp = [[-1] * (n+1) for i in xrange(m+1)]
        for i in xrange(1, m+1):
            if S[i-1] == T[0]:
                dp[i][1] = i-1
            else:
                dp[i][1] = dp[i-1][1]
        for i in xrange(1, m+1):
            for j in xrange(2, n+1):
                if S[i-1] == T[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = dp[i-1][j]
        minlen = float('inf')
        minst = -1
        for i in xrange(1, m+1):
            if dp[i][n] != -1:
                if i - dp[i][n] < minlen:
                    minlen = i - dp[i][n]
                    minst = dp[i][n]
        return S[minst:minst+minlen] if minst != -1 else "" 


class Solution(object):
    def minWindow(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        m = len(S)
        n = len(T)
        dp = [-1] * (m+1)
        for i in xrange(1, m+1):
            if S[i-1] == T[0]:
                dp[i] = i-1
            else:
                dp[i] = dp[i-1]
        for j in xrange(2, n+1):
            tmp = [-1] * (m+1)
            for i in xrange(1, m+1):   
                if S[i-1] == T[j-1]:
                    tmp[i] = dp[i-1]
                else:
                    tmp[i] = tmp[i-1]
            dp = tmp
        minlen = float('inf')
        minst = -1
        for i in xrange(1, m+1):
            if dp[i] != -1:
                if i - dp[i] < minlen:
                    minlen = i - dp[i]
                    minst = dp[i]
        return S[minst:minst+minlen] if minst != -1 else ""


                            
