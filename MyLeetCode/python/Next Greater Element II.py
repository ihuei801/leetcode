###
# Stack
# Time Complexity: O(n)
# Space Complexity: O(n)
###
class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        re = [-1] * len(nums)
        st = []
        for i in xrange(2*len(nums)):
            num = nums[i % len(nums)]
            while st and num > nums[st[-1]]:
                re[st.pop()] = num
            if i < len(nums):
                st.append(i)
        return re
                                        
                            
                    