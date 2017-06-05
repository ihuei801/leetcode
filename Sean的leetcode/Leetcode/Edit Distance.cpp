//https://leetcode.com/discuss/17997/my-accepted-java-solution
//https://www.youtube.com/watch?v=z_CB7Gih_Mg
class Solution {
public:
    int minDistance(string word1, string word2) {
        int m = word1.size();
        int n = word2.size();

        int dist[m+1][n+1];

        for (int i = 0; i < m+1; i++)
            dist[i][0] = i;
        for (int i = 0; i < n+1; i++)
            dist[0][i] = i;

        //i equal 0 is null character, i equal 1 is the index 0 of word1.
        for (int i = 1; i < m+1; i++)
            for (int j = 1; j < n+1; j++)
            {
                int cost = (word1[i-1] == word2[j-1]) ? 0 : 1;
                dist[i][j] = min(min(dist[i-1][j]+1, dist[i][j-1]+1), dist[i-1][j-1]+cost);
            }
        return dist[m][n];
    }
};