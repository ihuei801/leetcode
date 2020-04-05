class Solution {
public:   
    bool isValid(string s) {
        unordered_map<char, char> table = {{'(', ')'}, {'{', '}'}, {'[', ']'}};
        stack<char> st;
        for (auto c : s) {
            if (c == '(' || c == '{' || c == '[') {
                st.push(c);
            }
            else if (c == ')' || c == '}' || c == ']') {
                if (st.empty()) return false;
                char tmp = st.top();
                st.pop();
                if (table[tmp] != c) {
                    return false;
                }
            }
        }
        return st.empty();
    }
};

class Solution {
public:
    bool isValid(string s) {
        stack<char> st;
        for (int i = 0; i < s.size(); i++) {
            if (s[i] == '{' || s[i] == '[' || s[i] == '(') {
               st.push(s[i]); 
            }
            else if (!st.empty() && ((s[i] == '}' && st.top() == '{') || (s[i] == ']' && st.top() == '[') || (s[i] == ')' && st.top() == '('))) {
                st.pop();
            }
            else{
                return false;
            }
        }
        return st.empty();
    }
};