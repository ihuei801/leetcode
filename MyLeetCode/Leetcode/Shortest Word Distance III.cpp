// https://leetcode.com/discuss/50715/12-16-lines-java-c
class Solution {
public:
    int shortestWordDistance(vector<string>& words, string word1, string word2) {
        int min_dist = INT_MAX;
        int idx1 = -1, idx2 = -1;
        for (int i = 0; i < words.size(); i++)
        {
            if (words[i] == word1)
                idx1 = i;
            if (words[i] == word2)
            {
                //Shortest Word Distance III and I only differs in this line.
                //let idx1 get previous index value.
                if (word1 == word2)
                    idx1 = idx2;
                idx2 = i;
            }
            if (idx1 != -1 && idx2 != -1)
                min_dist = min(min_dist, abs(idx2 - idx1));
        }
        return min_dist;
    }
};