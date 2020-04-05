###
# DP: memoize
# Time Complexity: O(N^2) N restricted
# Space Complexity: O(N^2) N restricted
###
class Solution(object):
    def soupServings(self, N):
        """
        :type N: int
        :rtype: float
        """
        memo = dict()
        N = -(-N//25)
        if N >= 500:
            return 1
        return self.dfs(N, N, memo)
    
    def dfs(self, a, b, memo):
        if (a, b) in memo:
            return memo[(a, b)]
        if a <= 0 and b <= 0:
            return 0.5
        if a <= 0:
            return 1
        if b <= 0:
            return 0
        prob = 0.25*(self.dfs(a-4, b, memo) + self.dfs(a-3, b-1, memo) + self.dfs(a-2, b-2, memo) + self.dfs(a-1, b-3, memo))
        memo[(a, b)] = prob
        return prob
        
        
        
        
                                        
                            
                    