###
# Linked List
# https://leetcode.com/problems/linked-list-random-node/discuss/85659/Brief-explanation-for-Reservoir-Sampling
# Time Complexity: O(n)
# Space Complexity:O(n)
###
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):

    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.head = head
        

    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        num = 1
        cur = self.head.next
        re = self.head
        while cur:
            r = random.randint(0, num)
            if r == 0:
                re = cur
            num += 1
            cur = cur.next
        return re.val


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
                                        
                            
                    