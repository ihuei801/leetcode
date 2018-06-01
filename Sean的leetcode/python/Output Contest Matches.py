###
# In each round, the i-th team becomes "(" + team[i] + "," + team[n-1-i] + ")", and then there are half as many teams.
# Time Complexity: O(n)
# Space Complexity: O(n)
###
class Solution(object):
    def findContestMatch(self, n):
        """
        :type n: int
        :rtype: str
        """
        team = map(str, range(1, n+1))
        while n > 1:
            for i in xrange(n/2):
                team[i] = '({},{})'.format(team[i], team[n-1-i])
            n /= 2
        return team[0]
                                        
                            
                    