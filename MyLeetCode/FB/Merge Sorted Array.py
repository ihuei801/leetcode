###
# Time Complexity: O(m+n)
# Space Complexity: O(1)
###
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        r = m + n - 1
        i, j = m - 1, n - 1
        while j >= 0 and i >= 0:
            if nums2[j] >= nums1[i]:
                nums1[r] = nums2[j]
                j -= 1
            else:
                nums1[r] = nums1[i]
                i -= 1
            r -= 1
        while j >= 0:
            nums1[r] = nums2[j]
            j -= 1
            r -= 1
        
        
            