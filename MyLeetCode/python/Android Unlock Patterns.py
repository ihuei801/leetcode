###
# DFS (postorder)
# Cannot use memoize because each path with (cur, remain) has different visit set
# Time Complexity:O(n!) combination of all posible patterns sigma i=m~n 9!/i!(9-i)!
# Space Complexity:O(n) n:max pattern length
###
class Solution(object):
    def numberOfPatterns(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        cnt = 0
        skip = [[None] * 10 for i in xrange(10)]
        skip[1][9] = skip[9][1] = skip[3][7] = skip[7][3] = skip[2][8] = skip[8][2] = skip[4][6] = skip[6][4] = 5
        skip[1][3] = skip[3][1] = 2
        skip[3][9] = skip[9][3] = 6
        skip[7][9] = skip[9][7] = 8
        skip[1][7] = skip[7][1] = 4
        for i in xrange(m, n+1):
            cnt += self.dfs(1, i, [False]*10, skip) * 4
            cnt += self.dfs(2, i, [False]*10, skip) * 4
            cnt += self.dfs(5, i, [False]*10, skip)
        return cnt
    
    def dfs(self, cur, remain, visit, skip):      
        if remain == 1:
            return 1 
        visit[cur] = True
        cnt = 0
        for nxt in xrange(1, 10):
            if (not skip[cur][nxt] or visit[skip[cur][nxt]]) and not visit[nxt]:
                cnt += self.dfs(nxt, remain-1, visit, skip)
        visit[cur] = False  
        return cnt
        
        
class Solution(object):
    def numberOfPatterns(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        cnt = 0
        skip = [[None] * 10 for i in xrange(10)]
        skip[1][9] = skip[9][1] = skip[3][7] = skip[7][3] = skip[2][8] = skip[8][2] = skip[4][6] = skip[6][4] = 5
        skip[1][3] = skip[3][1] = 2
        skip[3][9] = skip[9][3] = 6
        skip[7][9] = skip[9][7] = 8
        skip[1][7] = skip[7][1] = 4
        for i in xrange(m, n+1):
            cnt += self.dfs(1, i, [False]*10, skip) * 4
            cnt += self.dfs(2, i, [False]*10, skip) * 4
            cnt += self.dfs(5, i, [False]*10, skip)
        return cnt
    
    def dfs(self, cur, remain, visit, skip):      
        if visit[cur]:
            return 0
        if remain == 1:
            return 1 
        visit[cur] = True
        cnt = 0
        for nxt in xrange(1, 10):
            if not skip[cur][nxt] or visit[skip[cur][nxt]]:
                cnt += self.dfs(nxt, remain-1, visit, skip)
        visit[cur] = False  
        return cnt





        


        