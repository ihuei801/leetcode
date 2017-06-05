class Solution {
public:
    string parseTernary(string expression) {
        int n = expression.size();
        stack<char> st;
        for (int i = n-1; i >= 0; i--) {
            char c = expression[i];
            if (!st.empty() && st.top() == '?') {
                st.pop();
                char first = st.top();
                st.pop();
                st.pop();
                char second = st.top();
                st.pop();
                if (c == 'T') {
                    st.push(first);
                }
                else {
                    st.push(second);
                }
            }
            else {
                st.push(c);
            }
        }
        char re = st.top();
        string s;
        s.push_back(re);
        return s;
    }
};