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
        from heapq import heappop, heappush
        if not lists:
            return None
        dummy = ListNode(None)
        cur = dummy
        pq = []
        for node in lists:
            if node:
                heappush(pq, (node.val, node))
        while pq:
            tmp = pq[0][1]
            heappop(pq)
            if tmp.next:
                heappush(pq, (tmp.next.val, tmp.next))
            cur.next = tmp
            cur = cur.next
        return dummy.next    