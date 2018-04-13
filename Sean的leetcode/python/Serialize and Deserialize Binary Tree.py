###
# DFS pre-order
# Time Complexity: O(n)
# Space Complexity: O(h) = O(n)
###

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        re = []
        self.serial(root, re)
        return ','.join(re)
        
    def serial(self, root, re):
        if not root:
            re.append("#")
            return
        re.append(str(root.val))
        self.serial(root.left, re)
        self.serial(root.right, re)
        
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        return self.deserial(iter(data.split(',')))
    
    def deserial(self, vals):
        val = next(vals)
        if val == "#":
            return None
        node = TreeNode(int(val))
        node.left = self.deserial(vals)
        node.right = self.deserial(vals)
        return node
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))