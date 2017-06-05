//refer http://fisherlei.blogspot.tw/2013/01/leetcode-triangle.html
//      http://jane4532.blogspot.tw/2013/09/triangleleetcode.html
//sum from bottom to up.
class Solution {
public:

    int minimumTotal(vector<vector<int> > &triangle) {

        for (int i = triangle.size()-2; i >= 0; i--)
            for (int j = 0; j < triangle[i].size(); j++)
            {
                triangle[i][j] += min(triangle[i+1][j], triangle[i+1][j+1]);
            }
        return triangle.empty() ? 0 : triangle[0][0];
    }
};