###
# Cyclic Sort
# Time Complexity: O(n)
# Space Complexity: O(1)
###
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):
            j = nums[i]
            if j < len(nums) and nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1
        for i, e in enumerate(nums):
            if i != e:
                return i
        return len(nums)
                    