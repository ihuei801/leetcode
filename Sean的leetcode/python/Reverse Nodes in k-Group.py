###
# Time Complexity: O(n)
# Space Complexity: O(1)
###
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or not head.next or k < 2:
            return head
        num = 0
        dummy = ListNode(0)
        dummy.next = head
        l = dummy
        curr = head
        while curr:
            num += 1
            if num % k == 0:
                l = self.reverse(l, curr.next)
                curr = l.next
            else:
                curr = curr.next
        return dummy.next
    def reverse(self, l, r):
        curr = tail = l.next
        pre = None
        while curr != r:
            next = curr.next
            curr.next = pre
            pre = curr
            curr = next
        l.next = pre
        tail.next = r
        return tail
                