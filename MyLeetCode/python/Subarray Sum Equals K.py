###
# Hash Table
# Time Complexity: O(n) 
# Space Complexity: O(n)
###
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if not nums:
            return 0
        accu = collections.defaultdict(int)
        accu[0] = 1
        cur_sum = 0
        cnt = 0
        for n in nums:
            cur_sum += n
            if cur_sum - k in accu:
                cnt += accu[cur_sum - k]
            accu[cur_sum] += 1
        return cnt
                                        
                            
                    