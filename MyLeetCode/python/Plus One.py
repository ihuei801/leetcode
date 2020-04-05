###
# Math
# Time Complexity: Worst case: O(n) 
# Space Complexity: O(1)
###
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if not digits:
            return []
        i = len(digits) - 1
        carry = 1
        while i >= 0:
            num = digits[i] + carry
            carry = num / 10
            digits[i] = num % 10
            if not carry:
                return digits
            i -= 1
        if carry:
            digits = [carry] + digits
        return digits
            
                                        
                            
                    