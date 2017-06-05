###
# Randomlize Quick Select
# Avg Time Complexity: O(n)
###
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        pivot = random.choice(nums)
        nums1, nums2 = [], []
        for num in nums:
            if num > pivot:
                nums1.append(num)
            elif num < pivot:
                nums2.append(num)
        if k <= len(nums1):
            return self.findKthLargest(nums1, k)
        elif k > len(nums) - len(nums2):
            return self.findKthLargest(nums2, k-(len(nums) - len(nums2)))
        else:
            return pivot
###
# Min heap
# Time Complexity: O(nlogk)
# Space Complexity: O(k)
###
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        from heapq import heappush, heappop
        q = []
        for e in nums:
            heappush(q, e)
            if len(q) > k:
                heappop(q)
        return q[0]