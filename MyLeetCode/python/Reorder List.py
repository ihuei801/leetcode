"""
Fast & Slow pointer
Time Complexity: O(n)
Space Complexity:O(1)
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return
        l1_end = self.find_mid(head)
        l2 = self.reverse(l1_end)
        p1 = head
        p2 = l2
        while p1 and p2:
            tmp = p1.next
            p1.next = p2
            p1 = tmp
            tmp = p2.next
            p2.next = p1
            p2 = tmp
        if p1:
            p1.next = None
        return head

    def find_mid(self, head):
        s = f = head
        while f and f.next:
            f = f.next.next
            s = s.next
        return s

    def reverse(self, head):
        pre = None
        p = head
        while p:
            nxt = p.next
            p.next = pre
            pre = p
            p = nxt
        return pre


                            
                    