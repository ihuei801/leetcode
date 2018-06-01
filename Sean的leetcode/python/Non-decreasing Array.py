###
# Array
# Consider all indices idx A[idx] > A[idx+1].
# If there are zero, the answer is True. 
# If there are 2 or more, the answer is False
# If there is one, we analyze the following cases:
# (1) if idx == 0, then we could make the array good by setting A[0] = A[1]
# (2) if idx == len(A) - 2. then we could make the array good by setting A[-1] = A[-2]
# (3) Otherwise, A[p-1], A[p], A[p+1], A[p+2] all exist
#     We could change A[p] to be between A[p-1] and A[p+1] if A[p-1] <= A[p+1]
#     We could change A[p+1] to be between A[p] and A[p+2] if A[p] <= A[p+2]
# Time Complexity: O(n) 
# Space Complexity: O(1)
###
class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        idx = None
        for i in xrange(len(nums)-1):
            if nums[i] > nums[i+1]:
                if idx is not None:
                    return False
                idx = i
        return idx is None or idx == 0 or idx == len(nums) - 2 or (nums[idx-1] <= nums[idx+1] or nums[idx] <= nums[idx+2])
        
        
        