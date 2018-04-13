###
# Two Pointers
# Time Complexity: O(n) 
# Space Complexity: O(1)
###
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ""
        s = list(s)
        l = 0
        r = len(s)-1
        vowels = "aeiouAEIOU"
        while l < r:
            if s[l] not in vowels:
                l += 1
            elif s[r] not in vowels:
                r -= 1
            else:
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1
        return ''.join(s)
                                        
                            
                    