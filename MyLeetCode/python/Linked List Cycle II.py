"""
Linked list - slow & fast pointers
Time Complexity: O(n)
Space Complexity: O(1)
Break the cycle to two part: a - both slow and fast passed by
                             b - only fast passed by
And the length outside the cycle is L
steps(slow) = L + a
steps(fast) = L + a + b + a = 2 (L + a) => b = L
So we will
(1) find the intersect
(2) use two pointers to start from head and intersect until they meet
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:      
        intersect = self.getIntersect(head)
        if not intersect:
            return None
        ptr1 = head
        ptr2 = intersect
        while ptr1 != ptr2:
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        return ptr1
        
    def getIntersect(self, head):   
        f = s = head
        while f and f.next:
            f = f.next.next
            s = s.next
            if s == f:
                return s.next
        return None
        