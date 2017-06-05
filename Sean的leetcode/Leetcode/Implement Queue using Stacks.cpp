class Queue {
public:
    // Push element x to the back of queue.
    void push(int x) {
        stk.push(x);
    }

    // Removes the element from in front of queue.
    void pop(void) {
        if (reverse_stk.empty())
            move_stack(stk, reverse_stk);
        reverse_stk.pop();
    }

    // Get the front element.
    int peek(void) {
        if (reverse_stk.empty())
            move_stack(stk, reverse_stk);
        return reverse_stk.top();
    }

    // Return whether the queue is empty.
    bool empty(void) {
        return stk.empty() && reverse_stk.empty();
    }

private:
    stack<int>stk;
    stack<int>reverse_stk;

    void move_stack(stack<int> &stk, stack<int> &reverse_stk)
    {
        while (!stk.empty())
        {
            int t = stk.top();
            reverse_stk.push(t);
            stk.pop();
        }
    }
};