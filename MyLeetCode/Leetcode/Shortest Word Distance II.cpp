//http://www.cnblogs.com/jcliBlogger/p/4705282.html
class WordDistance {
public:
    unordered_map<string, vector<int>> w_map;
    WordDistance(vector<string>& words) {
        int n = words.size();
        for (int i = 0; i < n; i++)
            w_map[words[i]].push_back(i);
    }

    int shortest(string word1, string word2) {
        vector<int> idx1 = w_map[word1];
        vector<int> idx2 = w_map[word2];
        int min_dist = INT_MAX;

        int len1 = idx1.size();
        int len2 = idx2.size();
        for (int i = 0, j = 0; i < len1 && j < len2;)
        {
            min_dist = min(min_dist, abs(idx1[i]-idx2[j]));
            if (idx1[i] < idx2[j])
                i++;
            else
                j++;
        }
        return min_dist;
    }
};

// Your WordDistance object will be instantiated and called as such:
// WordDistance wordDistance(words);
// wordDistance.shortest("word1", "word2");
// wordDistance.shortest("anotherWord1", "anotherWord2");