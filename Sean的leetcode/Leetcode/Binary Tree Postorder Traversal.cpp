/**
 * Definition for binary tree
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

//iterative solution: stack
class Solution {
public:
    vector<int> postorderTraversal(TreeNode *root) {
        stack<TreeNode*> s;
        TreeNode *top_node, *popped = 0;
        vector<int>res;

        res.clear();

        if (!root) return res;

        s.push(root);

        while (!s.empty())
        {
            top_node = s.top();

            if ((!top_node->right && !top_node->left)
                || (popped && popped == top_node->left)
                || (popped && popped == top_node->right))
            {
                res.push_back(top_node->val);
                s.pop();
                popped = top_node;
                continue;
            }

            if (top_node->right)
                s.push(top_node->right);

            if (top_node->left)
                s.push(top_node->left);

        }
        return res;
    }
};


//recursive solution
#if 0
class Solution {
public:

    vector<int> postorderTraversal(TreeNode *root) {
        vector<int>left, right;
        int i;

        left.clear();
        right.clear();

        if (!root) return left;

        left = postorderTraversal(root->left);
        right = postorderTraversal(root->right);

        left.insert(left.end(), right.begin(), right.end());
        left.insert(left.end(), 1, root->val);
        return left;
    }
};
#endif