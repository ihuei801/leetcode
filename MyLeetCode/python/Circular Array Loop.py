"""
Slow & Fast pointers
Time complexity: O(n**2)
Space complexity: O(1)
"""
class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        if len(nums) <= 1:
            return False
        for i, e in enumerate(nums):
            is_forward = nums[i] >= 0
            s = f = i
            while True:
                s = self.next_idx(s, nums, is_forward)
                f = self.next_idx(f, nums, is_forward)
                if f != -1:
                    f = self.next_idx(f, nums, is_forward)
                if s == -1 or f == -1 or s == f:
                    break
            if s != -1 and s == f:
                return True
        return False

    def next_idx(self, p, nums, is_forward):
        direc = nums[p] >= 0
        if is_forward != direc:
            return -1
        nxt_p = (p + nums[p]) % len(nums)
        if p == nxt_p:
            return -1
        return nxt_p


                    