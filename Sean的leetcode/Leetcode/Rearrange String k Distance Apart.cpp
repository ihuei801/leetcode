/* Greedy
 * count: count the number of characters
 * leftmost: the left most idx that a character can be put
 * select the character with the most count that can be put in the current position
 * Time Complexity: O(n)
 */
class Solution {
public:
    string rearrangeString(string str, int k) {
        int n = str.size();
        vector<int> count(26);
        vector<int> leftmost(26);
        for (auto c : str) {
            count[c - 'a']++;
        }
        string res;
        for (int i = 0; i < n; i++) {
            int idx = findMax(count, leftmost, i);
            if (idx == -1) return "";
            count[idx]--;
            leftmost[idx] = i + k;
            res += (char) ('a' + idx);
        }
        return res;
    }
    int findMax(vector<int>& count, vector<int>& leftmost, int pos) {
        int max = 0;
        int idx = -1;
        for (int i = 0; i < 26; i++) {
            if (count[i] > max && pos >= leftmost[i]) {
                max = count[i];
                idx = i;
            }
        }
        return idx;
    }
};