class Solution {
public:
    vector<vector<int>> generate(int numRows) {
        vector<int>one_row;
        vector<vector<int> >res;

        for (int i = 0; i < numRows; i++)
        {
            for (int j = 0; j <= i; j++)
            {
                if (j == 0 || j == i)
                    one_row.push_back(1);
                else
                    one_row.push_back(res[i-1][j-1]+res[i-1][j]);
            }
            res.push_back(one_row);
            one_row.clear();
        }
        return res;
    }
};