class Solution {
public:
    void compute(stack<int> &stk, string comp_type)
    {
        int x, y, res;
        y = stk.top();
        stk.pop();
        x = stk.top();
        stk.pop();
        
        if (comp_type.compare("+") == 0)
            res = x + y;
        else if (comp_type.compare("-") == 0)
            res = x - y;
        else if (comp_type.compare("*") == 0)
            res = x * y;
        else if (comp_type.compare("/") == 0)
            res = x / y;
            
        stk.push(res);
    }
    
    int evalRPN(vector<string> &tokens) {
        stack<int> stk;

        for (int i = 0; i < tokens.size(); i++)
        {
            if ((tokens[i].compare("+") == 0)
                || (tokens[i].compare("-") == 0)
                || (tokens[i].compare("*") == 0)
                || (tokens[i].compare("/") == 0))
                compute(stk, tokens[i]);
            else
                stk.push(atoi(tokens[i].c_str()));    
        }
        return stk.top();
    }
};