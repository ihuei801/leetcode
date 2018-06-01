###
# Array Stack
# Time Complexity: k * [O(n+m)+O(k)]      
###
class Solution(object):
    def maxNumber(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """
        re = []
        for l1 in xrange(max(0, k-len(nums2)), min(len(nums1), k)+1):
            re = max(re, self.merge(self.getmax(nums1, l1), self.getmax(nums2, k-l1)))
        return re
    
    def getmax(self, nums, l):
        rm = len(nums) - l
        re = []
        for n in nums:
            while re and rm and re[-1] < n:
                re.pop()
                rm -= 1
            re.append(n)
        return re[:l]
    
    def merge(self, nums1, nums2):
        re = []
        i = 0
        j = 0
        while i < len(nums1) or j < len(nums2):
            if i == len(nums1):
                re.append(nums2[j])
                j += 1
            elif j == len(nums2):
                re.append(nums1[i])
                i += 1
            else:
                if nums1[i] > nums2[j]:
                    re.append(nums1[i])
                    i += 1
                elif nums2[j] > nums1[i]:
                    re.append(nums2[j])
                    j += 1
                else:
                    k, l = i, j
                    while k < len(nums1) and l < len(nums2) and nums1[k] == nums2[l]:
                        k += 1
                        l += 1
                    if l == len(nums2) or (k < len(nums1) and nums1[k] > nums2[l]):
                        re.append(nums1[i])
                        i += 1
                    else:
                        re.append(nums2[j])
                        j += 1             
        return re
    
    
        