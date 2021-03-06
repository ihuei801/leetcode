###
# Time Complexity: O(n)
# Space Complexity: O(1)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head:
            return True

        l1_end = self.find_mid(head)
        l2 = self.reverse(l1_end)

        p1 = head
        p2 = l2
        while p1 and p2:
            if p1.val != p2.val:
                return False
            p1 = p1.next
            p2 = p2.next
        return True

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
