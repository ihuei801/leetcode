###
# Array Sort
# Time Complexity: O(nlogn) 
# Space Complexity: O(n)
###
class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        sort_nums = sorted(enumerate(nums), key=lambda (idx, num): num, reverse=True)
        re = [""] * len(nums)
        for i, (idx, num) in enumerate(sort_nums):  
            if i == 0:
                re[idx] = "Gold Medal"
            elif i == 1:
                re[idx] = "Silver Medal"
            elif i == 2:
                re[idx] = "Bronze Medal"
            else:
                re[idx] = str(i+1)
        return re
        
                                        
                            
                    