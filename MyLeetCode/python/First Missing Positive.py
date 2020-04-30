###
# Cyclic Sort
# Time Complexity: O(n)
# Space Complexity: O(1)
###
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):
            j = nums[i] - 1
            if j >= 0 and j < len(nums) and nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1
        for i, n in enumerate(nums):
            if n != i + 1:
                return i + 1
        return len(nums) + 1