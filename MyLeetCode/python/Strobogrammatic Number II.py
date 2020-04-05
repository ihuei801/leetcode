###
# Back Tracking
# Time Complexity: O(5^n) T(n) = 5T(n-2) 
# Space Complexity: O(n/2) recursive O(5^n) result
###
class Solution(object):
    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        return self.bt(n, n)
    def bt(self, n, target):   
        if n == 0:
            return [""]
        if n == 1:
            return ["0", "1", "8"]    
        re = []
        for word in self.bt(n-2, target):
            if n != target:
                re.append("0" + word + "0")
            re.append("1" + word + "1")
            re.append("8" + word + "8")
            re.append("6" + word + "9")
            re.append("9" + word + "6")
        return re
        
        