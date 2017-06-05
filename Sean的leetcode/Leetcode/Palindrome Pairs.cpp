//Use hashmap
//Split each word to two part and check whether the palindrome exists
//l    r    l'
//r'   l    r
//if l is empty: it could be l' l  r
//Time: O(n * k ^ 2)
class Solution {
public:
    vector<vector<int>> palindromePairs(vector<string>& words) {
        unordered_map<string, int> table;
        for (int i = 0; i < words.size(); i++) {
            string tmp = words[i];
            reverse(tmp.begin(), tmp.end());
            table[tmp] = i;
        }
        vector<vector<int>> re;
        for (int i = 0; i < words.size(); i++) {
            for (int j = 0; j < words[i].size(); j++){
                string l = words[i].substr(0, j);
                string r = words[i].substr(j);
                if(table.count(l) && table[l] != i && isPalindrome(r)){
                    re.push_back({i, table[l]});
                    if(l.empty()){
                        re.push_back({table[l], i});
                    }
                }
                if(table.count(r) && table[r] != i && isPalindrome(l)){
                    re.push_back({table[r], i});
                }
            }
        }
        return re;
        
    }
    bool isPalindrome(string& s){
        int n = s.size();
        if (n <= 1) return true;
        int l = 0, r = n-1;
        while (l < r) {
            if (s[l] != s[r]) return false;
            l++;
            r--;
        }
        return true;
    }
};