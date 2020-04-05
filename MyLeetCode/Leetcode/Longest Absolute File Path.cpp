/* Use a hashtable to report the len of the previous level
 *
 */
class Solution {
public:
    int lengthLongestPath(string input) {
        stringstream ss(input);
        string s;
        int maxlen = 0;
        unordered_map<int, int> table;
        table[0] = 0;
        
        while (getline(ss, s, '\n')) {
            int pos = s.find_first_not_of('\t');
            string name = s.substr(pos);
            int level = s.size() - name.size();
            if (name.find('.') == string::npos) {
                table[level + 1] = table[level] + name.size() + 1;
            }
            else {
                maxlen = max(maxlen, table[level] + (int)name.size()); 
            }
        }
        return maxlen;
    }
};