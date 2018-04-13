###
# Heap
# Time: O(klogk)
# Space: O(k)
###
class Value(object):
    def __init__(self, sum, i, j):
        self.sum = sum
        self.i = i
        self.j = j
    def __cmp__(self, other):
        if self.sum < other.sum:
            return -1
        elif self.sum > other.sum:
            return 1
        else:
            return 0
class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        from Queue import PriorityQueue
        if not nums1 or not nums2:
            return []
        q = PriorityQueue()
        q.put(Value(nums1[0] + nums2[0], 0, 0))
        re = []
        while not q.empty() and k:
            cur = q.get()
            re.append([nums1[cur.i], nums2[cur.j]])
            if cur.j + 1 < len(nums2):
                q.put(Value(nums1[cur.i] + nums2[cur.j + 1], cur.i, cur.j + 1))
            if cur.i + 1 < len(nums1) and cur.j == 0:
                q.put(Value(nums1[cur.i + 1] + nums2[cur.j], cur.i + 1, cur.j))
            
            k -= 1
        return re
        
        