###
# DP
# State: 
# equ: whether previous i digits is equal to prefix of N
# has_rot: whether previous i digits has a digit in "2569"
# Function:
# equ[i] = equ[i-1] and N[i] == d
# has_rot[i] = has_rot[i-1] or d in "2569"
# Initialization:
# equ[0] = True
# has_rot[0] = False
# Answer:
# when i == len(N): if has_rot[i]: return 1
# Time Complexity: O(logN)
# Space Complexity: O(logN)
###
class Solution(object):
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        N = map(int, str(N))
        memo = dict()
        return self.dp(N, 0, True, False, memo)
    
    def dp(self, N, idx, equ, has_rot, memo):
        if idx == len(N): 
            return int(has_rot)
        if (idx, equ, has_rot) in memo:
            return memo[(idx, equ, has_rot)]
        cnt = 0
        for d in xrange(N[idx]+1 if equ else 10): #the generated string can not be bigger than N
            if d in {3, 4, 7}:
                continue
            else:
                cnt += self.dp(N, idx+1, equ and d == N[idx], has_rot or d in {2,5,6,9}, memo)
            memo[(idx, equ, has_rot)] = cnt
        return cnt 

# Brute Force
# Time Complexity: O(nlogn) length of n = logn
# Space Complexity: O(1)
#
class Solution(object):
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        cnt = 0
        for i in xrange(1, N+1):
            num = str(i)
            cnt += int(all(c not in "347" for c in num) and any(c in "2569" for c in num))      
        return cnt
            
                                        
                             
                    