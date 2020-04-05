###
# Bit Manipulation
# Time Complexity: O(n)
# Space Complexity: O(1)
###
class Solution(object):
    def validUtf8(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """
        cnt = 0
        for b in data:
            if cnt:
                if (b >> 6) == 0b10:
                    cnt -= 1
                else:
                    return False
            else:
                if (b >> 5) == 0b110:
                    cnt = 1
                elif (b >> 4) == 0b1110:
                    cnt = 2
                elif (b >> 3) == 0b11110:
                    cnt = 3
                elif b >> 7:
                    return False
        return cnt == 0
                            
                    