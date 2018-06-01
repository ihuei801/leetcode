###
# Binary Search
# Time Complexity: O(nlogm+mlogn)
# Space Complexity: O(1)
###
class Solution(object):
    def minArea(self, image, x, y):
        """
        :type image: List[List[str]]
        :type x: int
        :type y: int
        :rtype: int
        """
        rows = len(image)
        cols = len(image[0])
        if not rows or not cols:
            return 0
        up = self.binary_search(image, 0, x, 0, cols-1, 'u')
        down = self.binary_search(image, x, rows-1, 0, cols-1, 'd')
        left = self.binary_search(image, up, down, 0, y, 'l')
        right = self.binary_search(image, up, down, y, cols-1, 'r')
        return ( down - up + 1) * (right - left + 1)
    
    def binary_search(self, image, si, ei, sj, ej, drc):
        if drc == 'u':
            l = si
            r = ei
            while l + 1 < r:
                mid = (l + r)/2
                if self.has_black(image, mid, mid, sj, ej):
                    r = mid
                else:
                    l = mid
            return l if self.has_black(image, l, l, sj, ej) else r
        elif drc == 'd':
            l = si
            r = ei
            while l + 1 < r:
                mid = (l + r)/2
                if self.has_black(image, mid, mid, sj, ej):
                    l = mid
                else:
                    r = mid      
            return r if self.has_black(image, r, r, sj, ej) else l
        elif drc == 'l':
            l = sj
            r = ej
            while l + 1 < r:
                mid = (l + r)/2
                if self.has_black(image, si, ei, mid, mid):
                    r = mid
                else:
                    l = mid
            return l if self.has_black(image, si, ei, l, l) else r
        else:
            l = sj
            r = ej
            while l + 1 < r:
                mid = (l + r)/2
                if self.has_black(image, si, ei, mid, mid):
                    l = mid
                else:
                    r = mid
            return r if self.has_black(image, si, ei, r, r) else l
        
    def has_black(self, image, si, ei, sj, ej):  
        return any(image[i][j]=="1" for i in xrange(si, ei+1) for j in xrange(sj, ej+1))
        
                                        
                            
                    