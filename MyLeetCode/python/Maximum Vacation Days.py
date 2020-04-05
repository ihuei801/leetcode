###
# DP
# State: dp[i][j] max vac days in week i, city j -> dp[j]
# Function: dp[i][j] = dp[i-1][k] + days[j][i] if k == j or flights[k][j] == 1 -> 1D: dp[j], max vac in city j
# Initialization: dp[0] = 0, dp[j] = INT_MIN for j != 0
# Answer: max(dp[j])
# Time Complexity: O(k*n^2) 
# Space Complexity: O(n)
###
class Solution(object):
    def maxVacationDays(self, flights, days):
        """
        :type flights: List[List[int]]
        :type days: List[List[int]]
        :rtype: int
        """
        N = len(days)
        k = len(days[0])
        vac = [-float('inf')] * N
        vac[0] = 0
        for i in xrange(k):
            tmp = [-float('inf')] * N
            for j in xrange(N):
                for pre in xrange(N):
                    if pre == j or flights[pre][j] == 1:
                        tmp[j] = max(tmp[j], vac[pre] + days[j][i])
            vac = tmp
            print vac
        return max(vac)
#######                                        
#DFS Memo
# Time Complexity: O(kn^2)
# Space Complexity: O(nk)
#####                            
class Solution(object):
    def maxVacationDays(self, flights, days):
        """
        :type flights: List[List[int]]
        :type days: List[List[int]]
        :rtype: int
        """
        
        N = len(days)
        k = len(days[0])
        memo = [[-float('inf')] * N for i in xrange(k) ]
        return self.dfs(flights, days, 0, 0, memo)
    
    def dfs(self, flights, days, week, city, memo):
        N = len(days)
        k = len(days[0])
        if week == k:
            return 0
        if memo[week][city] != -float('inf'):
            return memo[week][city]
        maxv = 0
        for j in xrange(N):
            if j == city or flights[city][j] == 1:
                v = days[j][week] + self.dfs(flights, days, week+1, j, memo)
                maxv = max(maxv, v)
        memo[week][city] = maxv        
        return maxv