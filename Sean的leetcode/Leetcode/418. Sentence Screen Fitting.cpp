/**
 * String s = String.join(" ", sentence) + " " ;. This line gives us a formatted sentence to be put to our screen.
 * start is the counter for how many valid characters from s have been put to our screen.
 * if (s.charAt(start % l) == ' ') is the situation that we don't need an extra space for current row. The current row could be successfully fitted. So that we need to increase our counter by using start++.
 * The else is the situation, which the next word can't fit to current row. So that we need to remove extra characters from next word.
 * start / s.length() is (# of valid characters) / our formatted sentence.
 */
class Solution {
public:
    int wordsTyping(vector<string>& sentence, int rows, int cols) {
        string s;
        for (string e : sentence) {
            s += e + ' ';
        }
        int n = s.size();
        int start = 0;
        for (int i = 0; i < rows; i++) {
            start += cols;
            if (s[start % n] == ' ') {
                start++;
            }
            else {
                while (start > 0 && s[(start - 1) % n] != ' ') {
                    start--;
                }
            }
        }
        return start / n;
    }
};