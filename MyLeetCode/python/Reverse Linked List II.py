###
# Linked List
# Time Complexity: O(n)
# Space Complexity: O(1)
###
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if m == n:
            return head
        pre = None
        cur = head
        pos = 1
        pre_end = nxt_start = None
        r_head = r_tail = None
        while cur:
            if pos == m:
                pre_end = pre
                r_head = cur
            elif pos == n:
                nxt_start = cur.next
                r_tail = cur
                break
            pre = cur
            cur = cur.next
            pos += 1

        r_head, r_tail = self.reverseList(r_head, r_tail)
        if pre_end:
            pre_end.next = r_head
        r_tail.next = nxt_start
        return head if pre_end else r_head

    def reverseList(self, head, tail):
        new_tail = head
        cur = head
        pre = None
        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            if cur == tail:
                break
            cur = nxt
        return pre, new_tail


        


        