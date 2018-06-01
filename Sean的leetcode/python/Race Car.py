###
# DP
# State: dp[i]: min num of instructions to move i steps start from abs(speed) = 1
# Function: dp[t] = dp[2**n-1-t] + n + 1 go pass the target and turn back A**(n)R + dp[2**n-1-t]
#           dp[t] = min(dp[t], dp[t-2**(n-1)+2**j] + n + j + 1) do not pass the target make two turns A**(n-1)RA**jR + dp[t - 2**(n-1) + 2**j] 
# Time Complexity: O(TlogT) 
# Space Complexity: O(T)
###
class Solution(object):
    def racecar(self, target):
        """
        :type target: int
        :rtype: int
        """
        memo = dict()
        return self.dfs(target, memo)
    def dfs(self, move, memo):
        if move == 0:
            return 0
        if move == 1:
            return 1
        if move in memo:
            return memo[move]
        n = move.bit_length()
        if move == 2**n-1:
            return n
        re = min(n + 1 + self.dfs(2**n-1-move, memo), min(n + j + 1 + self.dfs(move - 2**(n-1) + 2**j, memo) for j in xrange(n-1)))
        memo[move] = re
        return re
        
class Solution(object):
    def racecar(self, target):
        """
        :type target: int
        :rtype: int
        """
        #dp[i]: min num of instructions to move i steps start from abs(speed) = 1
        dp = [0, 1] + [float('inf')] * (target - 1)
        for t in xrange(2, target+1):
            n = t.bit_length()
            if t == 2**n -1:
                dp[t] = n
                continue
            #go pass the target and turn back A**(n)R + dp[2**n-1-t]
            dp[t] = dp[2**n-1-t] + n + 1
            #do not pass the target make two turns A**(n-1)RA**jR + dp[t - 2**(n-1) + 2**j]
            for j in xrange(n-1):
                dp[t] = min(dp[t], dp[t-2**(n-1)+2**j] + n + j + 1)   
        return dp[target]
                            
                    