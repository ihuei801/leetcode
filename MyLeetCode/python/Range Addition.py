###
# Array
# Time Complexity: hasNext:  O(k+n) k:operations, n: length
# Space Complexity: O(1)
# Note. if the elements are not the same, change the offset of the element:
# [2,3,10,5] transforms to [2, 1, 7, -5]
###
class Solution(object):
    def getModifiedArray(self, length, updates):
        """
        :type length: int
        :type updates: List[List[int]]
        :rtype: List[int]
        """
        re = [0] * length
        for s, e, v in updates:
            re[s] += v
            if e + 1 < length:
                re[e+1] -= v
        for i in xrange(1,length):
            re[i] += re[i-1]
        return re
                                        
                            
                    