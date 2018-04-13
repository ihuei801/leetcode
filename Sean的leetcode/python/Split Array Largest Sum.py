###
# Binary search
#The answer is between maximum value of input array numbers and sum of those numbers.
# Use binary search to approach the correct answer. We have l = max number of array; r = sum of all numbers in the array;Every time we do mid = (l + r) / 2;
# Use greedy to narrow down left and right boundaries in binary search.
# 3.1 Cut the array from left.
# 3.2 Try our best to make sure that the sum of numbers between each two cuts (inclusive) is large enough but still less than mid.
# 3.3 We'll end up with two results: either we can divide the array into more than m subarrays or we cannot.
# If we can, it means that the mid value we pick is too small because we've already tried our best to make sure each part holds as many non-negative numbers as we can but we still have numbers left. So, it is impossible to cut the array into m parts and make sure each parts is no larger than mid. We should increase m. This leads to l = mid + 1;
# If we can't, it is either we successfully divide the array into m parts and the sum of each part is less than mid, or we used up all numbers before we reach m. Both of them mean that we should lower mid because we need to find the minimum one. This leads to r = mid - 1;
# Time Complexity: O(log(sum-max)) * O(n)
# Space Complexity: O(1)
#
###
class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        max_val, s = 0, 0
        for num in nums:
            max_val = max(max_val, num)
            s += num
        l = max_val
        r = s
        while l + 1 < r:
            mid = (l + r)/2
            if self.valid(mid, nums, m):
                r = mid
            else:
                l = mid
        if self.valid(l, nums, m):
            return l
        else:
            return r
        
    def valid(self, boundary, nums, m):
        cnt = 1
        s = 0
        for num in nums:
            s += num
            if s > boundary:
                s = num
                cnt += 1
                if cnt > m:
                    return False
        return True
        