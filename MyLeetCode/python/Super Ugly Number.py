###
# Priority Queue
# Time Complexity: O(k) + O(nlogk)
# Space Complexity: O(k)
###
class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        import heapq
        length = len(primes)
        small_idx = [0] * length
        ugly = [1]
        q  = [(primes[i] * ugly[small_idx[i]], i) for i in xrange(len(primes))]
        heapq.heapify(q)
        while len(ugly) < n:
            tmp, idx = heapq.heappop(q)
            small_idx[idx] += 1
            if tmp != ugly[-1]:
                ugly.append(tmp)
            heapq.heappush(q, (primes[idx] * ugly[small_idx[idx]], idx))
        return ugly[-1] 
        
        