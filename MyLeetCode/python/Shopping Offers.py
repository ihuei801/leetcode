###
# Dynamic Programming
# Time Complexity:
# Space Complexity: 
###
class Solution(object):
    def shoppingOffers(self, price, special, needs):
        """
        :type price: List[int]
        :type special: List[List[int]]
        :type needs: List[int]
        :rtype: int
        """
        memo = dict()
        return self.dfs(needs, price, special, memo)
    
    def dfs(self, needs, price, special, memo):
        if tuple(needs) in memo:
            return memo[tuple(needs)]
        n = len(needs)
        cost = sum(need * price for need, price in zip(needs, price))
        for sp in special:
            if all(needs[i] >= sp[i] for i in xrange(n)):
                cost = min(cost, sp[-1] + self.dfs(tuple(needs[i] - sp[i] for i in xrange(n)), price, special, memo))
        memo[tuple(needs)] = cost
        return cost

                                        
                            
                    