// The length of the repeating substring must be a divisor of the length of the input string
// Search for all possible divisor of str.length, starting for length/2
// If i is a divisor of length, repeat the substring from 0 to i the number of times i is contained in s.length
// If the repeated substring is equals to the input str return true
class Solution {
public:
    bool repeatedSubstringPattern(string str) {
        int n = str.size();
        for (int l = n/2; l > 0; l--) {
            if (n % l == 0) {
                int m = n / l;
                string sub = str.substr(0, l);
                string s;
                for (int i = 0; i < m; i++) {
                    s += sub;
                }
                if (s == str) return true;
            }
        }
        return false;
    }
};