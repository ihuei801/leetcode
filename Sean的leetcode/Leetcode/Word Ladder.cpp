class Solution {
public:
    int ladderLength(string beginWord, string endWord, unordered_set<string>& wordList) {
        if (beginWord.empty() || endWord.empty() || wordList.empty()) return 0;
        queue<string> q;
        wordList.erase(beginWord);
        wordList.erase(endWord);
        int ladder = 1;
        if (beginWord == endWord) return 1;
        q.push(beginWord);
        while (!q.empty()) {
            int size = q.size();
            for (int i = 0; i < size; i++) {
                string tmp = q.front();
                q.pop();
                for (int j = 0; j < tmp.size(); j++) {
                    char c = tmp[j];
                    for (char k = 'a'; k <= 'z'; k++) {
                        if (k == c) continue;
                        tmp[j] = k;
                        if (tmp == endWord) {
                            return ladder + 1;
                        }
                        if (wordList.count(tmp)) {
                            wordList.erase(tmp);
                            q.push(tmp);
                        }
                    }
                    tmp[j] = c;
                }
            }
            ladder++;
        }
        return 0;
    }
};

// http://www.programcreek.com/2012/12/leetcode-word-ladder/
class Solution {
public:
    int ladderLength(string start, string end, unordered_set<string> &dict) {
        map<string, int>distance_map;
        queue<string>words;
        int distance;

        words.push(start);
        distance_map[start] = 1;
        dict.erase(start);

        while(!words.empty())
        {
            string str = words.front();
            words.pop();
            distance = distance_map[str];

            for (int i = 0; i < str.size(); i++)
            {
                //backup to restore
                char org = str[i];
                for (char c = 'a'; c <= 'z'; c++)
                {
                    if (str[i] == c)
                        continue;

                    str[i] = c;

                    if (str == end)
                        return distance+1;

                    if (dict.find(str) != dict.end())
                    {
                        words.push(str);
                        distance_map[str] = distance+1;
                        //important!! To avoid duplicate str inserted into queue<string>words.
                        //Remove the hit str in the dictionary.
                        dict.erase(str);
                    }
                }
                str[i] = org;
            }
        }
        return 0;
    }
};