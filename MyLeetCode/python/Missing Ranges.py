###
# Array
# Time Complexity: O(n)
# Space Complexity: O(n)
###
class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        pre = lower - 1
        nums.append(upper+1)
        re = []
        for n in nums:
            if n == pre + 2:
                re.append(str(pre+1))
            elif n > pre + 2:
                re.append(str(pre+1) + "->" + str(n-1))
            pre = n     
        return re
        
        