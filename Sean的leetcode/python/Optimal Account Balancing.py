###
# DFS
# Time Complexity: for N people, using at most N-1 transactions will guarantee to clear all debts. 
# So the question is in which order gives the optimal answer. 
# The DFS algorithm basically just exhausts all possible such orders. 
# To order N people with last two orderless, there are N!/2 ways. 
# So the algorithm should be O(N!). The worst case should be there is no subset which has overall net zero deb
# Space Complexity: O(n)
###
class Solution(object):
    def minTransfers(self, transactions):
        """
        :type transactions: List[List[int]]
        :rtype: int
        
        """
        
        bal = collections.defaultdict(int)
        for f, t, m in transactions:
            bal[f] -= m
            bal[t] += m
        bal = [e for e in bal.values() if e != 0]
        return self.dfs(bal, 0)
        
    def dfs(self, bal, s):
        res = float('inf')
        while s < len(bal) and bal[s] == 0:
            s += 1
        visit = set()
        for i in xrange(s+1, len(bal)):
            if bal[i] * bal[s] < 0 and bal[i] not in visit:
                bal[i] += bal[s]
                res = min(res, 1 + self.dfs(bal, s+1))
                bal[i] -= bal[s]
                visit.add(bal[i])
        return res if res != float('inf') else 0
                                        
                            
                    