###
# Hash Table 
# Time Complexity: O(n) - bucket sort O(nlogn) - sort
# Space Complexity: O(n)
###
# Method 1 - Bucket Sort
class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        from collections import Counter, defaultdict
        if not s:
            return ""
        d = Counter(s)
        b = defaultdict(list)
        re = ""
        for k, v in d.iteritems():
            b[v].append(k*v)
            
        return "".join(["".join(b[k]) for k in xrange(len(s), -1, -1) if k in b])
                                        
# Method 2 - Sort
class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        from collections import Counter
        if not s:
            return ""
        d = Counter(s)
        re = ""
        for k, v in sorted(d.iteritems(), key=lambda (k, v): v, reverse=True):
            re += k * v
        return re                    
                    