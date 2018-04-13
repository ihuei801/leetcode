class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = {}
        self.l = []

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.d:
            return False
        
        self.l.append(val)
        self.d[val] = len(self.l) - 1
        return True
        

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.d:
            return False
        rm_idx = self.d[val]
        self.d[self.l[-1]] = rm_idx
        self.l[rm_idx] = self.l[-1]
        self.d.pop(val)
        self.l.pop()
        return True

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        from random import randint
        return self.l[randint(0, len(self.l)-1)]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()