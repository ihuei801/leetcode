//https://leetcode.com/discuss/22500/best-solution-i-have-found-with-explanations
//Time O(mn), Space O(1)
class Solution {
public:
    int calculateMinimumHP(vector<vector<int>>& dungeon) {
        int row = dungeon.size();
        int col = dungeon[0].size();

        for (int i = row-1; i >= 0; i--)
            for (int j = col-1; j >= 0; j--)
            {
                //the bottom-right
                if (i == row-1 && j == col-1)
                    dungeon[i][j] = max(1, 1 - dungeon[i][j]);
                //the last row can only go left.
                else if (i == row-1)
                    dungeon[i][j] = max(1, dungeon[i][j+1] - dungeon[i][j]);
                //the last col can only go down.
                else if (j == col-1)
                    dungeon[i][j] = max(1, dungeon[i+1][j] - dungeon[i][j]);
                //others: can go left or down.
                else
                    dungeon[i][j] = max(1, min(dungeon[i][j+1], dungeon[i+1][j]) - dungeon[i][j]);
            }
        return dungeon[0][0];
    }
};