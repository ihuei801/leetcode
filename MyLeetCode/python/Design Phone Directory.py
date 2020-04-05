###
# Design
# Time Complexity: O(1)
# Space Complexity: O(n)
###
class PhoneDirectory(object):

    def __init__(self, maxNumbers):
        """
        Initialize your data structure here
        @param maxNumbers - The maximum numbers that can be stored in the phone directory.
        :type maxNumbers: int
        """
        self.max_num = maxNumbers
        self.avail = range(maxNumbers)
        self.used = set()

    def get(self):
        """
        Provide a number which is not assigned to anyone.
        @return - Return an available number. Return -1 if none is available.
        :rtype: int
        """
        if not self.avail:
            return -1
        num = self.avail.pop()
        self.used.add(num)
        return num

    def check(self, number):
        """
        Check if a number is available or not.
        :type number: int
        :rtype: bool
        """
        if number >= self.max_num or number < 0:
            return False
        if number in self.used:
            return False
        return True
        
    def release(self, number):
        """
        Recycle or release a number.
        :type number: int
        :rtype: void
        """
        if number in self.used:
            self.used.remove(number)
            self.avail.append(number)
        


# Your PhoneDirectory object will be instantiated and called as such:
# obj = PhoneDirectory(maxNumbers)
# param_1 = obj.get()
# param_2 = obj.check(number)
# obj.release(number)