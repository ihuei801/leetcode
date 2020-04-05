//Stack
class Solution {
public:
    string decodeString(string s) {
        stack<int> num_st;
        stack<string> str_st;
        int n = s.size();
        int num = 0;
        string res;
        for (int i = 0; i < n; i++) {
            if (isdigit(s[i])) {
                num = num * 10 + (s[i] - '0');
            }
            else if (s[i] == '[') {
                num_st.push(num);
                str_st.push(res);
                num = 0;
                res = "";
            }
            else if (s[i] == ']') {
                int pre_num = num_st.top();
                string pre_str = str_st.top();
                num_st.pop();
                str_st.pop();
                string tmp;
                for (int j = 0; j < pre_num; j++) {
                    tmp += res;
                }
                res = pre_str + tmp;
                num = 0;
                
            }
            else {
                res += s[i];
            }
            
        }
        return res;
    }
};
//dfs
class Solution {
public:
    string decodeString(string s) {
        int curr = 0;
        return decode(s, curr);
    }
    string decode(string& s, int& curr) {
        string res;
        while (curr < s.size() && s[curr] != ']') {
            if (!isdigit(s[curr])) {
                res += s[curr++];
            }
            else {
                int n = 0;
                while(curr < s.size() && isdigit(s[curr])) {
                    n = n * 10 + s[curr++] - '0';
                }
                curr++;
                string t = decode(s, curr);
                curr++;
                while (n--) {
                    res += t;
                } 
            }
        }
        return res;
    }
};