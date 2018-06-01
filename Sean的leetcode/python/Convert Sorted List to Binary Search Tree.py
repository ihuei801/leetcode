###
# Tree
###
######## Method1
# Inorder:
# Time Complexity: O(n)
# Space Complexity: O(1)
#####################################
# # Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if not head:
            return None
        cnt = 0
        cur = head
        while cur:
            cnt += 1
            cur = cur.next
        return self.dfs([head], 0, cnt-1)

    def dfs(self, head, start, end):
        
        if start > end:
            return None
        mid = (start + end) / 2 
        left = self.dfs(head, start, mid-1) 
        h = head[0]
        node = TreeNode(h.val)
        node.left = left
        head[0] = h.next
        node.right = self.dfs(head, mid+1, end)
        return node
        
### Method 2
# Preorder
# Time Complexity: T(n) = 2T(n/2) + O(n) O(nlogn)
# Space complexity: O(logn)
###
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if not head:
            return None
        return self.dfs(head, None)

    def dfs(self, head, tail):
        if not head or head == tail:
            return None
        slow = fast = head
        while fast != tail and fast.next != tail:
            slow = slow.next
            fast = fast.next.next

        node = TreeNode(slow.val)
        node.left = self.dfs(head, slow) 
        node.right = self.dfs(slow.next, tail)
        return node
        
                                        
                            
                    