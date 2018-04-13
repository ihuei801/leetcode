###
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
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        idx = 0
        while idx < n:
            buf4 = [""] * 4
            buf_cnt = read4(buf4)
            buf_idx = 0
            while idx < n and buf_idx < buf_cnt:
                buf[idx] = buf4[buf_idx]
                idx += 1
                buf_idx += 1
            if buf_cnt < 4:
                break
        return idx
            