###
# Linked List
# Time Complexity: O(n) 
###
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def plusOne(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        newhead = ListNode(0)
        newhead.next = head
        cur = newhead
        ptr = newhead
        while cur:
            if cur.val != 9:
                ptr = cur
            cur = cur.next
        ptr.val += 1
        cur = ptr.next
        while cur:
            cur.val = 0
            cur = cur.next
        return newhead if newhead.val != 0 else newhead.next
        
        