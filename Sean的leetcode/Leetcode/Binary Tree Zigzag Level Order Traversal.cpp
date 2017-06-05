//refer http://leetcode.com/2010/09/printing-binary-tree-in-zig-zag-level_18.html
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    void genStack(stack<TreeNode*> &pop_stk, stack<TreeNode*> &push_stk, vector<int> &one_row, int dir)
    {
        while (!pop_stk.empty())
        {
            TreeNode* top = pop_stk.top();
            pop_stk.pop();

            one_row.push_back(top->val);

            if (dir == 0)
            {
                if (top->left)
                    push_stk.push(top->left);
                if (top->right)
                    push_stk.push(top->right);
            }
            else
            {
                if (top->right)
                    push_stk.push(top->right);
                if (top->left)
                    push_stk.push(top->left);
            }
        }
    }

    vector<vector<int>> zigzagLevelOrder(TreeNode* root) {
        vector<int> one_row;
        vector<vector<int> > res;
        stack<TreeNode*> stk[2];
        int curr = 0;

        if (!root) return res;

        stk[curr].push(root);

        while (!stk[curr].empty() || !stk[1-curr].empty())
        {
            genStack(stk[curr], stk[1-curr], one_row, curr);
            res.push_back(one_row);
            one_row.clear();
            curr ^= 1;
        }
        return res;
    }
};