###
# Hash Table 
# Time Complexity: O(n) - bucket sort; O(nlogn) - sort
# Space Complexity: O(n)
###
# Method 1 - Bucket Sort
class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ""
        cnt = collections.Counter(s)
        n = len(s)
        bucket = collections.defaultdict(list)
        for k, v in cnt.iteritems():
            bucket[v].append(k*v)  
        return "".join("".join(bucket[i]) for i in xrange(n, -1, -1) if i in bucket)
                                        
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
                    