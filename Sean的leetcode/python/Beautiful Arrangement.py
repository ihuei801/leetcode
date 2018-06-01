###
# BFS
# Time Complexity: O(k) k : number of valid permutation
# Space Complexity: O(n)
###   
class Solution(object):
    def countArrangement(self, N):
        """
        :type N: int
        :rtype: int
        """
        visit = [False] * (N+1)
        self.cnt = 0
        self.bt(N, 1, visit)
        return self.cnt
    
    def bt(self, N, pos, visit):
        if pos > N:
            self.cnt += 1
            return
        for i in xrange(1, N+1):
            if not visit[i] and (i % pos == 0 or pos % i == 0):
                visit[i] = True
                self.bt(N, pos+1, visit)
                visit[i] = False
            
            
                    
        
                            
   