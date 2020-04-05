###
# Two Pointers
# Time Complexity: O(n)
# Space Complexity: O(n)
###
class Solution(object):
    def largeGroupPositions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]
        """
        r = 0
        re = []
        while r < len(S):
            if r == 0 or S[r] != S[r-1]:
                l = r
                while r+1 < len(S) and S[r+1] == S[r]:
                    r += 1
                if r - l + 1 >= 3:
                    re.append([l, r])
            r += 1
        return re
                                        
                            
class Solution(object):
    def largeGroupPositions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]
        """
        r = 0
        l = 0
        re = []
        while r < len(S):
            if r == len(S)-1 or S[r] != S[r+1]: 
                if r - l + 1 >= 3:
                    re.append([l, r])
                l = r+1
            r += 1
        return re