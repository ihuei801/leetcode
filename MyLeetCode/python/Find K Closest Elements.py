###
# Binary Search + Two Pointers
# Time Complexity: O(logn + k)
# Space Complexity: O(k) #slice arr to return
###
class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        if not arr:
            return []
        
        if x >= arr[-1]:
            return arr[-k:]
        elif x <= arr[0]:
            return arr[:k]
        idx = bisect.bisect(arr, x)
        l = idx - 1
        r = idx
        while r - l - 1 < k:
            if l < 0:
                r += 1
            elif r == len(arr):
                l -= 1
            else:
                if abs(arr[l] - x) <= abs(arr[r] - x):
                    l -= 1
                else:
                    r += 1
        return arr[l+1:r]
                
        