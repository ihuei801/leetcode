###
# Array
# Time Complexity: O(n)
# Space Complexity: O(n)
###
class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:
            return []
        re = []
        pre = nums[0]
        for i, n in enumerate(nums):
            if i == len(nums) - 1 or nums[i+1] != n + 1:
                if pre == n:
                    re.append(str(pre))
                else:
                    re.append(str(pre) + "->" + str(n))
                if i != len(nums) - 1:
                    pre = nums[i+1]
        return re
                
        
        