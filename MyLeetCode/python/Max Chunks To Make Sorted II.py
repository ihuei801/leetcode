###
# Array
# Iterate through the array, each time all elements to the left are smaller (or equal) to all elements to the right, there is a new chun
# Time Complexity: O(n)
# Space Complexity: O(n)
###
class Solution(object):
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        if not arr:
            return 0
        n = len(arr)
        l_max = [0] * n
        r_min = [0] * n
        l_max[0] = arr[0]
        r_min[-1] = arr[-1]
        for i, e in enumerate(arr):
            if i == 0:
                l_max[i] = e
                r_min[n-1-i] = arr[n-1-i]
            else:   
                l_max[i] = max(l_max[i-1], e)
                r_min[n-1-i] = min(r_min[n-i], arr[n-1-i])
        cnt = 1
        for i in xrange(n-1):
            if l_max[i] <= r_min[i+1]:
                cnt += 1
        return cnt
        
                            
                    