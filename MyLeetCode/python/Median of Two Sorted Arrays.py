###
# Binary Search
# Binary search. Call 2 times getkth and k is about half of (m + n). 
# Every time call getkth can reduce the scale k to its half. So the time complexity is log(m + n).
# Time Complexity: O(log(m+n))
# Space Complexity: O(log(m+n))
###
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m = len(nums1)
        n = len(nums2)
        if m + n & 1:
            return self.findkth(nums1, nums2, (m+n)/2 + 1)
        else:
            return (self.findkth(nums1, nums2, (m+n)/2) + self.findkth(nums1, nums2, (m+n)/2+1))/2.0
        
    def findkth(self, nums1, nums2, k):
        m = len(nums1)
        n = len(nums2)
        if m > n:
            return self.findkth(nums2, nums1, k)
        if m == 0:
            return nums2[k-1]
        if k == 1:
            return min(nums1[0], nums2[0])
        i = min(k/2, m)
        j = k - i
        if nums1[i-1] < nums2[j-1]:
            return self.findkth(nums1[i:], nums2, k-i)
        else:
            return self.findkth(nums1, nums2[j:], k-j)






 
                                        
                            
                    