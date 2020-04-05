###
# Read multiple times:
# Store the buf of last read4 
# Terminate condition:
# 1) read n characters
# 2) no character to read
# Time Complexity: O(n)
# Space Complexity: O(n)
###
# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution(object):
    def __init__(self):
        self.buf4 = [None] * 4
        self.buf_idx = 0
        self.buf_num = 0
        
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """   
        idx = 0
        while idx < n:
            EOF = False
            if self.buf_idx == self.buf_num:
                self.buf_num = read4(self.buf4)
                self.buf_idx = 0
            while self.buf_idx < self.buf_num and idx < n:
                buf[idx] = self.buf4[self.buf_idx]
                self.buf_idx += 1
                idx += 1
            if self.buf_num < 4:
                return idx
        return idx