###
# Time Complexity:O(nk)
# Space Complexity:O(1)
###
class Solution(object):
    def minCostII(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if not costs or not costs[0]:
            return 0
        n = len(costs)
        k = len(costs[0])
        min1, min2 = -1, -1
        for i in xrange(n):
            last1, last2 = min1, min2
            min1, min2 = -1, -1
            for j in xrange(k):
                if j != last1:
                    costs[i][j] += 0 if last1 < 0 else costs[i-1][last1]
                else:
                    costs[i][j] += 0 if last2 < 0 else costs[i-1][last2]
                if min1 < 0 or costs[i][j] < costs[i][min1]:
                    min2 = min1
                    min1 = j
                elif min2 < 0 or costs[i][j] < costs[i][min2]:
                    min2 = j
        return costs[n-1][min1]
                    