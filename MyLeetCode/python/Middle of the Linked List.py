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
    def middleNode(self, head: ListNode) -> ListNode:
        s = f = head
        while f and f.next:
            f = f.next.next
            s = s.next
        return s


                            
                    