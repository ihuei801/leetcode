###
# Array 
# The basic idea is to use max[] array to keep track of the max value until the current position, 
# and compare it to the sorted array (indexes from 0 to arr.length - 1). 
# If the max[i] equals the element at index i in the sorted array, then the final count++.
# For example,
# original: 0, 2, 1, 4, 3, 5, 7, 6
# max:      0, 2, 2, 4, 4, 5, 7, 7
# sorted:   0, 1, 2, 3, 4, 5, 6, 7
# index:    0, 1, 2, 3, 4, 5, 6, 7
# The chunks are: 0 | 2, 1 | 4, 3 | 5 | 7, 6
# Time Complexity: O(n)
# Space Complexity: O(1)
###
class Solution(object):
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        if not arr:
            return 0
        cur_max = 0
        cnt = 0
        for i, e in enumerate(arr):
            cur_max = max(cur_max, e)
            if cur_max == i:
                cnt += 1
        return cnt
                
                                
                    