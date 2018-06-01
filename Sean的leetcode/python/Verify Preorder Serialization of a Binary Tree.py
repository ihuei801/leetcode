###
# Tree
# Time Complexity: O(n)
# Space Complexity: O(n)
###
class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        if not preorder:
            return True
        out = 1
        for node in preorder.split(','):
            out -= 1
            if out < 0:
                return False
            if node != "#":
                out += 2
        return out == 0


                                        
                            
                    