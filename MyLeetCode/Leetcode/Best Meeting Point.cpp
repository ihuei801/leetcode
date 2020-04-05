//O(mn)
class Solution {
public:
    int minTotalDistance(vector<vector<int>>& grid) {
        int row = grid.size();
        int col = grid[0].size();
        vector<int> rowpos;
        vector<int> colpos;
        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++){
                if (grid[i][j] == 1) {
                    rowpos.push_back(i);
                }
            }
        }
        for (int j = 0; j < col; j++) {
            for (int i = 0; i < row; i++) {
                if (grid[i][j] == 1) {
                    colpos.push_back(j);
                }
            }
        }
        return getDis(rowpos) + getDis(colpos);
    }
    
    int getDis(vector<int>& pos){
        int re = 0;
        int i = 0;
        int j = pos.size() - 1;
        while (i < j) {
            re += pos[j--] - pos[i++];
        }
        return re;
    }
    
};