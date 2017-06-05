/* DFS
 * Limit max removal rmL and rmR for backtracking boundary. Otherwise it will exhaust all possible valid substrings, not shortest ones.
 * Scan from left to right, avoiding invalid strs (on the fly) by checking num of open parens.
 * If it's '(', either use it, or remove it.
 * If it's '(', either use it, or remove it.
 * Otherwise just append it.
*/
class Solution {
public:
    vector<string> removeInvalidParentheses(string s) {
        int l_rm = 0, r_rm = 0;
        unordered_set<string> res;
        int size = s.size();
        for (int i = 0; i < size; i++) {
            if (s[i] == '(') {
                l_rm++;
            }
            else if (s[i] == ')') {
                if (l_rm != 0) {
                    l_rm--;
                }
                else {
                    r_rm++;
                }
            }
        }
        dfs(s, 0, l_rm, r_rm, 0, "", res);
        return vector<string> (res.begin(), res.end());
    }
    void dfs(string s, int idx, int l_rm, int r_rm, int stack, string path, unordered_set<string>& res) {
       
        int size = s.size();
        if (idx == size) {
            if (l_rm == 0 && r_rm == 0 && stack == 0) {
                res.insert(path);
            }
            return;
        }
       
        if (s[idx] == '(') {
            if (l_rm){
                dfs(s, idx + 1, l_rm - 1, r_rm, stack, path, res);
            }
            dfs(s, idx + 1, l_rm, r_rm, stack + 1, path + s[idx], res);
        }
        else if (s[idx] == ')') {
            if (r_rm){
                dfs(s, idx + 1, l_rm, r_rm - 1, stack, path, res);
            }
            if (stack) {
                dfs(s, idx + 1, l_rm, r_rm, stack - 1, path + s[idx], res);
            }
        }
        else{
            dfs(s, idx + 1, l_rm, r_rm, stack, path + s[idx], res); 
        }
       
    }
};