###
# Two Pointer
# Time Complexity: O(n)
# Space Complexity: O(n)
###
class Solution(object):
    def sortTransformedArray(self, nums, a, b, c):
        """
        :type nums: List[int]
        :type a: int
        :type b: int
        :type c: int
        :rtype: List[int]
        """
        if not nums:
            return []
        re = [0] * len(nums)
        l = 0
        r = len(nums) - 1
        idx = len(nums) - 1 if a > 0 else 0
        while l <= r:
            lv = self.fn(nums[l], a, b, c)
            rv = self.fn(nums[r], a, b, c)
            if a > 0:
                if lv > rv:
                    re[idx] = lv
                    idx -= 1
                    l += 1
                else:
                    re[idx] = rv
                    idx -= 1
                    r -= 1
            else:
                if lv < rv:
                    re[idx] = lv
                    idx += 1
                    l += 1
                else:
                    re[idx] = rv
                    idx += 1
                    r -= 1
        return re
    def fn(self, x, a, b, c):
        return a*x**2 + b*x + c
                                        
                            
                    