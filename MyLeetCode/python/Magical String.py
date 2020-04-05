###
# String
# Create an int array a and initialize the first 3 elements with 1, 2, 2.
# Create the pointer to the number which will be used to generate new numbers.
# A trick to flip number back and forth between 1 and 2: num = num ^ 3
# Time Complexity: hasNext:  O(n)
# Space Complexity: O(n)
###
class Solution(object):
    def magicalString(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0:
            return 0
        if n <= 3:
            return 1
        s = [1,2,2]
        i = 2
        cnt = 1
        while len(s) < n:
            if s[-1] ^ 3 == 1:
                cnt += min(s[i], n-len(s))
            s += [(s[-1] ^ 3)] * s[i]
            i += 1
        return cnt
                                        
                            
                    