###
# Stack
# Time Complexity: next: O(1) hasNext:O(n)
# Space Complexity: O(n)
###
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.stack = [[nestedList, 0]]

    def next(self):
        """
        :rtype: int
        """
        if self.hasNext():
            lst, i = self.stack[-1]
            self.stack[-1][1] += 1
            return lst[i].getInteger()
        else:
            return -1
        

    def hasNext(self):
        """
        :rtype: bool
        """
        s = self.stack
        while s:
            lst, i = s[-1]
            if i == len(lst):
                s.pop()
            else:
                e = lst[i]
                if e.isInteger():
                    return True
                s[-1][1] += 1
                s.append([e.getList(), 0])
        return False

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())