###
# Array Vitual index
# Time Complexity: O(n)
# Space Complexity: O(1)
###
class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        random.shuffle(nums)
        if len(nums) <= 1:
            return 
        mid = self.findKthSmallest(nums, -(-len(nums)//2))
        def newidx(i):
            return (1 + 2*i) % (len(nums) | 1)
        l = 0
        r = len(nums) - 1
        i = 0
        while i <= r:
            if nums[newidx(i)] > mid:
                nums[newidx(l)], nums[newidx(i)] = nums[newidx(i)], nums[newidx(l)]
                i += 1
                l += 1
            elif nums[newidx(i)] < mid:
                nums[newidx(r)], nums[newidx(i)] = nums[newidx(i)], nums[newidx(r)]
                r -= 1
            else:
                i += 1
    
    
    # def findKthSmallest(self, nums, k):
    #     """
    #     :type nums: List[int]
    #     :type k: int
    #     :rtype: int
    #     """
    #     pivot = random.choice(nums)
    #     nums1, nums2 = [], []
    #     for num in nums:
    #         if num < pivot:
    #             nums1.append(num)
    #         elif num > pivot:
    #             nums2.append(num)
    #     if k <= len(nums1):
    #         return self.findKthSmallest(nums1, k)
    #     elif k > len(nums) - len(nums2):
    #         return self.findKthSmallest(nums2, k-(len(nums) - len(nums2)))
    #     else:
    #         return pivot
    def findKthSmallest(self, nums, k):
        if not nums:
            return None
        pos = self.partition(nums, 0, len(nums)-1)
        if k < pos+1:
            return self.findKthSmallest(nums[:pos], k)
        elif k > pos+1:
            return self.findKthSmallest(nums[pos+1:], k-pos-1)
        else:
            return nums[pos]
        
    def partition(self, nums, l, r):
        # idx = random.randint(l, r)
        # nums[idx], nums[r] = nums[r], nums[idx]
        for i in xrange(l, r):
            if nums[i] < nums[r]:
                nums[l], nums[i] = nums[i], nums[l]
                l += 1
        nums[l], nums[r] = nums[r], nums[l]
        return l
                
                                        
                            
                    