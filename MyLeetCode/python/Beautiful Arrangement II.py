###
# Two Pointers
# if you have n number, the maximum k can be n - 1;
# if n is 9, max k is 8.
# This can be done by picking numbers interleavingly from head and tail,
# k = 1 [1,2,3,4,5,6,7,8,9]
# k = 2 [9,1,2,3,4,5,6,7,8]
# k = 3 [1,9,2,3,4,5,6,7,8]
# ...
# k = 8 [9,1,8,2,7,3,6,4,5]
# Time Complexity: O(n)
# Space Complexity: O(n)
###
class Solution(object):
    def constructArray(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[int]
        """
        res = []
        l, r = 1, n
        while l <= r:
            if k > 1:
                if k & 1:
                    res.append(l)
                    l += 1
                else:
                    res.append(r)
                    r -= 1
                k -= 1
            else:
                res.append(l)
                l += 1
        return res
                                        
                            
                    