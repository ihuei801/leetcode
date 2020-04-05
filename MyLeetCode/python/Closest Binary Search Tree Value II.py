
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
        if not root:
            return []

        pred = self.init_pred(root, target)
        succ = self.init_succ(root, target)
        result = []
        print(pred)
        print(succ)
        while k:
            if not pred:
                result.append(self.get_next_succ(succ))
            elif not succ:
                result.append(self.get_next_pred(pred))
            else:
                if abs(pred[-1].val - target) < abs(succ[-1].val - target):
                    result.append(self.get_next_pred(pred))
                else:
                    result.append(self.get_next_succ(succ))
            k -= 1
        return result

    def init_pred(self, root, target):
        pred = []
        cur = root
        while cur:
            if cur.val <= target:
                pred.append(cur)
                cur = cur.right
            else:
                cur = cur.left
        return pred

    def init_succ(self, root, target):
        succ = []
        cur = root
        while cur:
            if cur.val > target:
                succ.append(cur)
                cur = cur.left
            else:
                cur = cur.right
        return succ

    def get_next_pred(self, pred):
        top = pred.pop()
        cur = top.left
        while cur:
            pred.append(cur)
            cur = cur.right
        return top.val

    def get_next_succ(self, succ):
        top = succ.pop()
        cur = top.right
        while cur:
            succ.append(cur)
            cur = cur.left
        return top.val


