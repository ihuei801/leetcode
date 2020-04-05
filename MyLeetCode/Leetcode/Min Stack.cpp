class MinStack {
public:
    stack<int>stk;
    stack<int>min_stk;

    void push(int x) {
        //be careful: it is "<=" instead of "<" because if x is equal min,
        //we still need to store it in min_stk for pop() usage.
        if (min_stk.empty() || x <= min_stk.top())
        {
            min_stk.push(x);
        }
        stk.push(x);
    }

    void pop() {
        if (stk.empty()) return;
        if (stk.top() == min_stk.top())
            min_stk.pop();
        stk.pop();
    }

    int top() {
        return st.empty()? -1 : st.top();
    }

    int getMin() {
        return minst.empty()? -1 : minst.top();
    }
};