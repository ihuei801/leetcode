###
# Linkedlist
# Scanning through the list, if node.val is in G and node.next.val isn't (including if node.next is null),
# then this must be the end of a connected component.
# For example, if the list is 0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7, 
# and G = [0, 2, 3, 5, 7], then when scanning through the list,
# we fulfill the above condition at 0, 3, 5, 7, for a total answer of 4.
# Time Complexity: O(n)
# Space Complexity: O(g)
###
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def numComponents(self, head, G):
        """
        :type head: ListNode
        :type G: List[int]
        :rtype: int
        """
        G = set(G)
        cur = head
        cnt = 0
        while cur:
            if cur.val in G and (not cur.next or cur.next.val not in G):
                cnt += 1
            cur = cur.next
        return cnt
                            
                    