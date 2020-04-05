###
# Greedy Stack
# Time Complexity: O(n)
# Space Complexity: O(n)
###
class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return s
        from collections import Counter
        cnt = Counter(s)
        visit = set()
        re = []
        for c in s:
            cnt[c] -= 1
            if c in visit:
                continue
            while re and re[-1] > c and cnt[re[-1]]:
                visit.remove(re[-1])
                re.pop()
            visit.add(c)
            re.append(c)     
        return ''.join(re)
        
                                        
                            
                    