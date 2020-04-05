class Solution:
    # @param s, a string
    # @return an integer
    def lengthOfLastWord(self, s):
        if (s == ''):
            return 0;
        word = s.split();
        if (len(word) == 0):
            return 0;
        else:
            return len(word[-1]);
