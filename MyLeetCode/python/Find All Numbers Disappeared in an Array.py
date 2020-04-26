###
# Cyclic Sort
# Time Complexity: O(n)
# Space Complexity: O(1)
###
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        i = 0
        while i < len(nums):
            j = nums[i] - 1
            if nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1
        result = []
        for i, n in enumerate(nums):
            if i != n - 1:
                result.append(i + 1)
        return result

