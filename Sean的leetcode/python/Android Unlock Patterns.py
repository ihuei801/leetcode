
###
# DFS (preorder)
# Time Complexity:O(n!) combination of all posible patterns sigmai=m~n 9!/i!(9-i)!
# Space Complexity:O(n) n:max pattern length
###
class Solution(object):
    def numberOfPatterns(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        skip = [[0] * 10 for i in xrange(10)]
        skip[1][3] = skip[3][1] = 2
        skip[1][7] = skip[7][1] = 4
        skip[3][9] = skip[9][3] = 6
        skip[7][9] = skip[9][7] = 8
        skip[1][9] = skip[9][1] = skip[3][7] = skip[7][3] = skip[2][8] = skip[8][2] = skip[4][6] = skip[6][4] = 5
        cnt = 0
        for i in xrange(m, n+1):
            cnt += self.dfs([False]*10, 1, i, skip) * 4
            cnt += self.dfs([False]*10, 2, i, skip) * 4
            cnt += self.dfs([False]*10, 5, i, skip)
        return cnt
    def dfs(self, visit, cur, remain, skip):
        if visit[cur]:
            return 0
        if remain == 1:
            return 1
        visit[cur] = True
        cnt = 0
        for n in xrange(1, 10):
            if not skip[cur][n] or visit[skip[cur][n]]:
                cnt += self.dfs(visit, n, remain-1, skip)
        visit[cur] = False
        return cnt
        