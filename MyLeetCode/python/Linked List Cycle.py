"""
LinkedList - Fast & slow pointer
Time Complexity: O(n)
Space Complexity: O(1)
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        f = s = head
        while f and f.next:
            f = f.next.next
            s = s.next
            if f == s:
                return True
        return False

