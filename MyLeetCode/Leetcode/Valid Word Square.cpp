class Solution {
public:
    bool validWordSquare(vector<string>& words) {
        int rows = words.size();
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < words[i].size(); j++) {
                if (j >= rows || i >= words[j].size() || words[i][j] != words[j][i]) return false;
            }
        }
        return true;
    }
};