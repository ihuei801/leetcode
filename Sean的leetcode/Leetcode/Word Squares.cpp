class Solution {
public:
    vector<vector<string>> wordSquares(vector<string>& words) {
        int n = words.size();
        vector<vector<string>> squares;
        if (n == 0) return squares;
        int size = words[0].size();
        vector<string> square(size);
        unordered_map<string, vector<string>> table;
        for (auto word : words) {
            for (int i = 0; i < word.size(); i++) {
                table[word.substr(0, i)].push_back(word);
            }
        }
        build(table, square, squares, 0, size);
        return squares;
    }
    void build(unordered_map<string, vector<string>>& table, vector<string>& square, vector<vector<string>>& squares, int i, int target) {
        if (i == target) {
            squares.push_back(square);
            return;
        }
        string prefix;
        for (int k = 0; k < i; k++) {
            prefix += square[k][i];
        }
        for (auto word: table[prefix]) {
            square[i] = word;
            build(table, square, squares, i+1, target);
        }
    }
};