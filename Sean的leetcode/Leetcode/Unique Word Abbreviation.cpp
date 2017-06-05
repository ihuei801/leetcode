class ValidWordAbbr {
public:
    unordered_map<string, unordered_set<string>> table;
    ValidWordAbbr(vector<string> &dictionary) {
        for (string s : dictionary) {
            int n = s.size();
            string key;
            if (n <= 2) {
                key = s;
            }
            else{
                key = s[0] + to_string(n-2) + s[n-1];
            }
            table[key].insert(s);
        }
    }

    bool isUnique(string word) {
        int n = word.size();
        string key;
        if (n <= 2) {
            key = word;
        }
        else {
            key = word[0] + to_string(n-2) + word[n-1];
        }
        return (!table.count(key) || table[key].count(word) == table[key].size());
        
    }
};


// Your ValidWordAbbr object will be instantiated and called as such:
// ValidWordAbbr vwa(dictionary);
// vwa.isUnique("hello");
// vwa.isUnique("anotherWord");
//https://leetcode.com/discuss/61546/8-lines-in-c
class ValidWordAbbr {
public:
    unordered_map<string, unordered_set<string>> d_map;
    ValidWordAbbr(vector<string> &dictionary) {
        for (auto w : dictionary)
        {
            if (w != "")
                d_map[w[0]+to_string(w.size()-2)+w[w.size()-1]].insert(w);
            else
                d_map[""].insert("");
        }
    }

    bool isUnique(string word) {
        string s;
        if (word == "") {
            s = "";
        }
        else{
            s = word[0] + to_string(word.size()-2) + word[word.size()-1];
        }
        return !d_map.count(s) || d_map[s].size() == d_map[s].count(word);
    }
};


// Your ValidWordAbbr object will be instantiated and called as such:
// ValidWordAbbr vwa(dictionary);
// vwa.isUnique("hello");
// vwa.isUnique("anotherWord");