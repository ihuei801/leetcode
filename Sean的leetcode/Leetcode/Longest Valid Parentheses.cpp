#if 1
//stack solution
//Time Complexity:O(n)
//left: the right most index of the unmatched substring
class Solution {
public:
    int longestValidParentheses(string s) {
        int left = -1;
        int size = s.size();
        stack<int> st;
        int maxlen = 0;
        for (int i = 0; i < size; i++) {
            if (s[i] == '(') {
                st.push(i);
            }
            else {
                if (st.empty()) {
                    left = i;
                }
                else {
                    st.pop();
                    if (st.empty()) {
                        maxlen = max(maxlen, i - left);
                    } 
                    else {
                        maxlen = max(maxlen, i - st.top());
                    }
                }
            }
        }
        return maxlen;
    }
};

//Sean
//1. use left_index to record the most left index when stack is emtpy.
//2. push '(' into stack
//3. pop '(' when input is ')'
//3.1 when the stack is not empty, the valid length is i - stk.top().
//3.2 when the stack is empty, the valid length is i - left_index + 1.
//4. reset the most left index when invalid sequence happens (i.e. stack is empty and input is ')').
class Solution {
public:
    int longestValidParentheses(string s) {
        int max_len = 0;
        stack<int>stk;
        int left_index = -1;

        for (int i = 0; i < s.size(); i++)
        {
            if (s[i] == '(')
            {
                if (left_index == -1)
                    left_index = i;
                stk.push(i);
            }
            else
            {
                if (!stk.empty())
                {
                    stk.pop();
                    if (!stk.empty())
                        max_len = max(max_len, i - stk.top());
                    else
                        max_len = max(max_len, i - left_index + 1);
                }
                else
                    left_index = -1;
            }
        }
        return max_len;
    }
};
#elif 1
//https://leetcode.com/discuss/44024/a-simple-c-dp-solution-without-stack-8ms-in-8-lines
//DP solution: dp[i] the longest valid length located at index i.
class Solution {
public:
    int longestValidParentheses(string s) {
        vector<int> dp(s.size(), 0);
        int max_len = 0;
        for (int i = 1; i < s.size(); i++)
        {
            int pair_idx = i - dp[i-1] - 1;
            if (s[i] == ')' && pair_idx >= 0 && s[pair_idx] == '(')
            {
                dp[i] = dp[i-1] + 2;
                if (pair_idx - 1 >= 0)
                    dp[i] += dp[pair_idx - 1];
                max_len = max(max_len, dp[i]);
            }
        }
        return max_len;
    }
};
#endif