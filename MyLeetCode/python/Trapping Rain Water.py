###
# Two Pointers
# Time: O(n)
# Space: O(1)
###
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) <= 1:
                return 0
        lh = rh = 0
        l = 0
        r = len(height) - 1
        water = 0
        while l < r:
            lh = max(lh, height[l])
            rh = max(rh, height[r])
            if lh < rh:
                water += lh - height[l] 
                l += 1
            else:
                water += rh - height[r]
                r -= 1
        return water
        
        