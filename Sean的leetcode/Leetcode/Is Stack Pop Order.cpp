bool isPopOrder(vector<int>pushOrder, vector<int>popOrder)
{
    stack<int> stk;
    int push_idx = 0;
    int pop_idx = 0;

    if (pushOrder.size() == 0 || popOrder.size() == 0)
        return false;

    while (1)
    {
        if (!stk.empty() && stk.top() == popOrder[pop_idx])
        {
            stk.pop();
            pop_idx++;
        }
        else
        {
            if (push_idx >= pushOrder.size())
                break;
            stk.push(pushOrder[push_idx]);
            push_idx++;
        }
    }

    if (stk.size() == 0 && pop_idx == popOrder.size())
        return true;
    else
        return false;
}
