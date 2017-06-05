/* Greedy
 * Time Complexity: O(n)
 * cnt: number of each character
 * visit: character is appear in the res string
 */
class Solution {
public:
    string removeDuplicateLetters(string s) {
        string res;
        vector<int> cnt(256, 0);
        vector<bool> visit(256, false);
        for (auto c : s) {
            cnt[c]++;
        }
        for (auto c : s) {
            cnt[c]--;
            if (visit[c]) continue;
            while (!res.empty() && c < res.back() && cnt[res.back()]) {
                visit[res.back()] = false;
                res.pop_back();
            }
            visit[c] = true;
            res += c;
        }
        return res;
    }
};