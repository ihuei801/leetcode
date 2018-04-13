###
# Time Complexity:O(nk)
# Space Complexity:O(1)
###
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
        min1 = min2 = -1
        for i in xrange(len(costs)):
            new_min1 = new_min2 = -1
            for j in xrange(len(costs[0])):
                if j != min1:
                    costs[i][j] += 0 if i == 0 else costs[i-1][min1]
                else:
                    costs[i][j] += 0 if i == 0 else costs[i-1][min2]
                if new_min1 < 0 or costs[i][j] < costs[i][new_min1]:
                    new_min2 = new_min1
                    new_min1 = j
                elif new_min2 < 0 or costs[i][j] < costs[i][new_min2]:
                    new_min2 = j
            min1, min2 = new_min1, new_min2
        return costs[len(costs)-1][min1]
                    
                    