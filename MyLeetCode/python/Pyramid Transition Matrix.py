###
# DFS + Backtracking(get cand)
# Time Complexity: O(A^(n^2)) T(n) = T(n-1) * A^(n-1) = A^(n^2) n: length of bottom. A: avg number of possible top
# Space Complexity: O(A^n)
###
class Solution(object):
    def pyramidTransition(self, bottom, allowed):
        """
        :type bottom: str
        :type allowed: List[str]
        :rtype: bool
        """
        if not bottom or not allowed:
            return False
        d = collections.defaultdict(list)
        for l, r, t in allowed:      #O(A)
            d[l+r].append(t)
        return self.dfs(bottom, d)    
    
    def dfs(self, bottom, d):
        if len(bottom) == 1:
            return True
        if any(bottom[idx:idx+2] not in d for idx in xrange(len(bottom)-1)):
            return False
        return any(self.dfs(cand, d) for cand in self.get_cand(bottom, d))
    
    def get_cand(self, bottom, d):
        re = []
        self.bt(bottom, 0, "", d, re)
        return re
    
    def bt(self, bottom, idx, one_sol, d, re):
        if idx+1 == len(bottom):
            re.append(one_sol)
            return 
        for b in d[bottom[idx:idx+2]]:
            self.bt(bottom, idx+1, one_sol+b, d, re)
            
            
            
            
            
                
                                        
                            
                    