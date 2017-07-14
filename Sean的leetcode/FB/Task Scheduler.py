###
#Time Complexity: O(n)
#Space Complexity: O(1)
###
class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        from heapq import heappush, heappop
        d = collections.defaultdict(int)
        for t in tasks:
            d[t] += 1
        q = []
        for t, cnt in d.iteritems():
            heappush(q, (-cnt, t))
        stage = 0
        while q:
            k = n+1
            tmp_list = []
            while k and q:
                cnt, t = heappop(q)
                cnt = -cnt
                
                if cnt > 1:
                    tmp_list.append((-(cnt-1), t))
                k -= 1
                stage += 1
            if tmp_list:
                for e in tmp_list:
                    heappush(q, e)        
                stage += k
                    
        return stage
        