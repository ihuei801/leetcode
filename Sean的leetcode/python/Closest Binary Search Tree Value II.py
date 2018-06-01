
###
# Tree Inorder
# Time Complexit: O(h+k)
# Space Complexity: O(h)
###
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def closestKValues(self, root, target, k):
        """
        :type root: TreeNode
        :type target: float
        :type k: int
        :rtype: List[int]
        """
        if not root or not k:
            return []
        pred, succ = [], []
        self.init_pred(root, target, pred)
        self.init_succ(root, target, succ)
        re = []
        while k:
            if not pred:
                re.append(self.get_next_succ(succ))
            elif not succ:
                re.append(self.get_next_pred(pred))
            else:
                if abs(pred[-1].val - target) < abs(succ[-1].val - target):
                    re.append(self.get_next_pred(pred))
                else:
                    re.append(self.get_next_succ(succ))
            k -= 1
        return re
    def init_pred(self, root, target, pred):
        cur = root
        while cur:
            if cur.val <= target:
                pred.append(cur)
                cur = cur.right
            else:
                cur = cur.left
    def init_succ(self, root, target, succ):
        cur = root
        while cur:
            if cur.val > target:
                succ.append(cur)
                cur = cur.left
            else:
                cur = cur.right
    def get_next_pred(self, pred):
        tmp = pred.pop()
        cur = tmp.left
        while cur:
            pred.append(cur)
            cur = cur.right
        return tmp.val
    def get_next_succ(self, succ):
        tmp = succ.pop()
        cur = tmp.right
        while cur:
            succ.append(cur)
            cur = cur.left
        return tmp.val