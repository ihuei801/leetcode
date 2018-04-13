#######################################################################
# Priority Queue
# Time Complexity: O(nk*log k) k:num of lists n: num of elements
# Heap implementation: http://algorithms.tutorialhorizon.com/binary-min-max-heap/
# A binary heap is a heap data struc­ture cre­ated using a binary tree.
# Two rules -
# 1) Shape property: Binary heap has to be om­plete binary tree at all lev­els except the last level.
# 2) Heap property: All nodes are either greater than equal to (Max-Heap) or less than equal to (Min-Heap) to each of its child nodes. 
# Heap insert/delete: O(log n)
#
# Python heappop, heappush
# You can use tuples, and it will sort by the first element of the tuple
#######################################################################
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        from Queue import PriorityQueue
        if not lists:
            return None
        pq = PriorityQueue()
        for lst in lists:
            if lst:
                pq.put((lst.val, lst))
        
        dummy = cur = ListNode(None)
        while not pq.empty():
            v, nd = pq.pop()
            cur.next = nd
            cur = cur.next
            if nd.next:
                pq.put((nd.next.val, nd.next))
        return dummy.next
            
        
            
        