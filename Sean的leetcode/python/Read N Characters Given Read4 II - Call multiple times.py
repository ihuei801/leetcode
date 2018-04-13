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
        self.buf4 = [""] * 4
        self.buf_cnt = 0
        self.buf_idx = 0
        
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        idx = 0
        while idx < n:
            if self.buf_idx == 0:
                self.buf_cnt = read4(self.buf4)
            while idx < n and self.buf_idx < self.buf_cnt:
                buf[idx] = self.buf4[self.buf_idx]
                idx += 1
                self.buf_idx += 1
            if self.buf_idx == self.buf_cnt:
                self.buf_idx = 0
            if self.buf_cnt < 4:
                break
        return idx