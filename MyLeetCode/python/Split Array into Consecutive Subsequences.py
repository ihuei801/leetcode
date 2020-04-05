###
# Greedy: HashTable
# Time Complexity: O(n)
# Space Complexity: O(n)
###
class Solution(object):
    def isPossible(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return False
        cnt = collections.Counter(nums)
        tails = collections.Counter()
        for n in nums:
            if cnt[n] == 0:
                continue
            if tails[n-1] > 0:
                tails[n-1] -= 1
                tails[n] += 1  
            elif cnt[n+1] > 0 and cnt[n+2] > 0:
                tails[n+2] += 1
                cnt[n+1] -= 1
                cnt[n+2] -= 1
            else:
                return False
            cnt[n] -= 1
        return True
        
                                        
                            
                    