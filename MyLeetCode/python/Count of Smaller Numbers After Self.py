###
# Merge Sort
# Time Complexity: O(nlogn)
# Space Complexity: O(logn) + O(n)
###
class Solution(object):
    def merge_sort(self, nums, start, end, small):
        if end - start <= 1:
            return 
        mid = (start + end) / 2
        self.merge_sort(nums, start, mid, small)
        self.merge_sort(nums, mid, end, small)
        j = mid
        for idx, n in nums[start:mid]:
            while j < end and nums[j][1] < n:
                j += 1               
            small[idx] += (j - mid)
        nums[start:end] = sorted(nums[start:end], key=lambda (idx, v): v) #use TimSort to sort the already sorted two subarray, O(n)
            
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        small = [0] * len(nums)
        self.merge_sort(list(enumerate(nums)), 0, len(nums), small)
        return small
    

class Solution(object):
    def merge_sort(self, nums, start, end, small):
        if end - start <= 1:
            return 
        mid = (start + end) / 2
        self.merge_sort(nums, start, mid, small)
        self.merge_sort(nums, mid, end, small)
        tmp = [0] * (end - start)
        j = mid
        k = 0
        for i in xrange(start, mid):
            while j < end and nums[j][1] < nums[i][1]:
                tmp[k] = nums[j]
                k += 1
                j += 1               
            small[nums[i][0]] += (j - mid)
            tmp[k] = nums[i]
            k += 1          
        for i in xrange(k):
            nums[start+i] = tmp[i]
            
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        small = [0] * len(nums)
        self.merge_sort(list(enumerate(nums)), 0, len(nums), small)
        return small
    
    
    
    
                                        
                            
                    