###
# String
# (1) Build out a string of words seperate by ' ' s
# (2) start is the pointer to the current characters from s
# (3) if s[start % l] == ' ' : we don't need an extra space for current row. 
#     The current row could be successfully fitted. So that we need to increase our counter by using start++.
#     else: next word can't fit to current row. So that we need to remove extra characters from next word.
# (4) start / s.length() is (# of valid characters) / our formatted sentence.
# Time Complexity: O(rows*cols)
# Space Complexity: O(sentence)
###
class Solution(object):
    def wordsTyping(self, sentence, rows, cols):
        sentence = ' '.join(sentence) + ' '
        start = 0
        for i in xrange(rows):
            start += cols
            if sentence[start % len(sentence)] == ' ':
                start += 1
            else:
                while start > 0 and sentence[(start-1) % len(sentence)] != ' ':
                    start -= 1
                    
        return start / len(sentence)
                                        
                            
                    