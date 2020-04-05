###
# Binary Search Tree 
# Overlap cannot be overlapped
# Time Complexity: Book: O(nlogm)
# Space Complexity: O(n + m) 
###
class MyCalendarTwo(object):

    def __init__(self):
        self.times = []
        
    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        overlaps = MyCalendar() #initialize calendar everytime; otherwise those that cannot be book will be stored in overlaps
        for s, e in self.times:
            if max(s, start) < min(e, end): #overlap
                if not overlaps.book(max(s, start), min(e, end)):
                    return False
        self.times.append((start, end))
        return True
            
class Node(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.left = None
        self.right = None
    def insert(self, start, end):
        if start >= self.end:
            if not self.right:
                self.right = Node(start, end)
                return True     
            return self.right.insert(start, end)
        elif end <= self.start:
            if not self.left:
                self.left = Node(start, end)
                return True
            return self.left.insert(start, end)        
        else:
            return False
    
class MyCalendar(object):
    def __init__(self):
        self.root = None
    def book(self, start, end):
        if not self.root:
            self.root = Node(start, end)
            return True    
        return self.root.insert(start, end)

# class MyCalendar(object):
#     def __init__(self):
#         self.times = []
#     def book(self, start, end):
#         for s, e in self.times:
#             if max(s, start) < min(e, end): #overlap
                    
#                     return False
#         self.times.append((start, end))
#         return True
# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)
                                        
                            
                    