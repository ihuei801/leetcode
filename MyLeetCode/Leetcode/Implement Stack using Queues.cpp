//https://leetcode.com/discuss/39747/two-queue-c-solutions-with-explaination
class Stack {
public:
    queue<int> q[2]; //q[curr] always keeps one element
    int curr = 0;

    // Push element x onto stack.
    void push(int x) {
        if (q[curr].empty())
            q[curr].push(x);
        else
        {
            while (!q[curr].empty())
            {
                q[1-curr].push(q[curr].front());
                q[curr].pop();
            }
            q[curr].push(x);
        }
    }

    // Removes the element on top of the stack.
    void pop() {
        q[curr].pop();
        while (q[1-curr].size() > 1)
        {
            q[curr].push(q[1-curr].front());
            q[1-curr].pop();
        }
        curr ^= 1;
    }

    // Get the top element.
    int top() {
        return q[curr].front();
    }

    // Return whether the stack is empty.
    bool empty() {
        return q[0].empty() && q[1].empty();
    }
};