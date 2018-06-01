###
# 
# Time Complexity: hasNext:  O(1) next O(1)
# Space Complexity: O(n)
###
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        q = -1
        l, r = 0, 0
        n = len(nums)
        maxlen = 0
        while r < n:
            if nums[r] == 0:
                if q != -1:
                    l = q
                q = r + 1
            maxlen = max(maxlen, r - l + 1)
            r += 1
        return maxlen
                                        
# Follow up                           
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        k = 1
        l = 0
        q = collections.deque()
        max_len = 0
        for r in xrange(len(nums)):
            if nums[r] == 0:
                q.append(r)
            if len(q) > k:
                l = q.popleft() + 1
            max_len = max(max_len, r - l + 1)
        return max_len