###
# Array
# Time Complexity: O(n^3)
# Space Complexity: O(sol*4)
###
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if len(nums) < 4:
            return []
        n = len(nums)
        nums.sort()
        re = []
        self.N_sum(nums, 0, target, 4, [], re)
        return re
                        
    def N_sum(self, nums, idx, target, N, one_sol, re):
        n = len(nums)
        if idx >= n or n-idx < N or nums[idx] * N > target or nums[n-1] * N < target:
            return
        if N == 2:
            l, r = idx, n-1
            while l < r:
                summ = nums[l] + nums[r]
                if summ == target:
                    re.append(one_sol+[nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1
                elif summ > target:
                    r -= 1
                else:
                    l += 1
        else:
            for i in xrange(idx, n):
                if i != idx and nums[i] == nums[i-1]:
                    continue
                self.N_sum(nums, i+1, target-nums[i], N-1, one_sol + [nums[i]], re)
                                        
                            
                    