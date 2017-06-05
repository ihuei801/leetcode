//https://leetcode.com/discuss/51543/java-o-n-and-o-1-extra-space
//Space: O(n)
//Idea: 5, [1, 2, 3] [7, 8, 9]: push 5, [1, 2, 3] into stack until stack.top() < preorder[i].
//Then pop all elements in stack smaller than preorder[i] to get the boundary value (here is 5).
//So, subsequent elements should be larger than the boundary value.
class Solution {
public:
    bool verifyPreorder(vector<int> preorder) {
        int low = INT_MIN;
        stack<int> path;
        for (auto p : preorder) {
            if (p < low)
                return false;
            while (!path.empty() && p > path.top())
            {
                low = path.top();
                path.pop();
            }
            path.push(p);
        }
        return true;
    }
};
