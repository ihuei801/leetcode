###
# BFS: ensure that upper level is printed before lower level
# Time Complexity: O(nlogn) (sorted dict)
# Space Complexity: O(n)
###
###
# Solution 1    
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        q = collections.deque([(root, 0)])
        d = collections.defaultdict(list)
        while q:
            node, idx = q.popleft()
            d[idx].append(node.val)
            if node.left:
                q.append((node.left, idx-1))
            if node.right:
                q.append((node.right, idx+1))
        return [d[k] for k in sorted(d)]
### 
# Solution 2
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        
        if not root:
            return []
        d = collections.defaultdict(list)
        q = [(0, root)]
        while q:
            next_q = []
            for idx, e in q:
                d[idx].append(e.val)
                if e.left:
                    next_q.append((idx-1, e.left))
                if e.right:
                    next_q.append((idx+1, e.right))
            q = next_q
        return [d[i] for i in sorted(d)]

            