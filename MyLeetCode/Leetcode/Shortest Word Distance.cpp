//https://leetcode.com/discuss/50234/ac-java-clean-solution
class Solution {
public:
    int shortestDistance(vector<string>& words, string word1, string word2) {
        int min_dist = INT_MAX;
        int w1_pos = -1, w2_pos = -1;
        int n = words.size();
        for (int i = 0; i < n; i++)
        {
            if (words[i] == word1)
                w1_pos = i;
            if (words[i] == word2)
                w2_pos = i;
            if (w1_pos >= 0 && w2_pos >= 0)
                min_dist = min(min_dist, abs(w1_pos - w2_pos));
        }
        return min_dist;
    }
};