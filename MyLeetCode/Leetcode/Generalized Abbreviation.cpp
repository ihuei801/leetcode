/* DFS backtracking
 * for every character, we can keep it or abbreviate it. 
 * To keep it, we add it to the current solution and carry on backtracking. 
 * To abbreviate it, we omit it in the current solution, but increment the count, which indicates how many characters have we abbreviated. 
 * When we reach the end or need to put a character in the current solution, and count is bigger than zero, we add the number into the solution.
 */
class Solution {
public:
    vector<string> generateAbbreviations(string word) {
        vector<string> res;
        if (word.empty()) return {""};
        string path;
        dfs(word, 0, 0, path, res);
        return res;
    }
    void dfs(string& word, int pos, int sum, string path, vector<string>& res) {
        if (pos == word.size()) {
            if (sum) {
                path += to_string(sum);
            }
            res.push_back(path);
            return;
        }
        dfs(word, pos+1, sum+1, path, res);
        dfs(word, pos+1, 0, path + (sum > 0? to_string(sum) : "") + word[pos], res);
    }
};