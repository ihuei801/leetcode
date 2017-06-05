//refer to http://fisherlei.blogspot.tw/2013/01/leetcode-unique-paths.html
class Solution {
public:
    int uniquePaths(int m, int n) {
        vector<int> count(n, 0);
        
        count[0] = 1;
        
        for (int i = 0; i < m; i++)
            for (int j = 1; j < n; j++)
                count[j] += count[j-1];
        return count[n-1];                
    }
};