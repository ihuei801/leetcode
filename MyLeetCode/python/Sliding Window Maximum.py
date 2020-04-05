###
# Deque
# Time Complexity: O(n) every element insert/delete once
# Space Complexity: O(k)
###
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        from collections import deque
        w = deque()
        re = []
        for i, n in enumerate(nums):
            # move left end
            if w and w[0] == nums[i - k]:
                w.popleft()
            # insert element
            while w and w[-1] < n:
                w.pop()
            w.append(n)
            if i >= k-1:
                re.append(w[0])
        return re
        
        