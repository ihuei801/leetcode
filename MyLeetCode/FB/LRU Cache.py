###
# Ordereddict: implemented by doubly linked list
###
from collections import OrderedDict
class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.table = OrderedDict()
        
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.table:
            value = self.table.pop(key)
            self.table[key] = value
            return value
        else:
            return -1
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.table:
            self.table.pop(key)
        elif len(self.table) == self.capacity:
            self.table.popitem(last=False)
        self.table[key] = value
        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


###
# HashTable + Doublylinkedlist
###
from collections import OrderedDict
class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.table = OrderedDict()
        
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.table:
            value = self.table.pop(key)
            self.table[key] = value
            return value
        else:
            return -1
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.table:
            self.table.pop(key)
        elif len(self.table) == self.capacity:
            self.table.popitem(last=False)
        self.table[key] = value
        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)