#if 1//morris traversal, O(1) space.
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
    vector<int> preorderTraversal(TreeNode* root) {
        vector<int> res;
        TreeNode *curr = root;

        while (curr)
        {
            if (curr->left)
            {
                TreeNode *p = curr->left;
                while (p->right && p->right != curr)
                    p = p->right;

                if (!p->right)
                {
                    res.push_back(curr->val);
                    p->right = curr;
                    curr = curr->left;
                }
                else
                {
                    p->right = 0;
                    curr = curr->right;
                }
            }
            else
            {
                res.push_back(curr->val);
                curr = curr->right;
            }
        }
        return res;
    }
};
#elif 1
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
    vector<int> preorderTraversal(TreeNode *root) {

        stack<TreeNode*> s;
        TreeNode *top_node;
        vector<int>res;

        res.clear();

        if (!root) return res;

        s.push(root);

        while (!s.empty())
        {
            top_node = s.top();
            res.push_back(top_node->val);
            s.pop();

            if (top_node->right)
                s.push(top_node->right);

            if (top_node->left)
                s.push(top_node->left);
        }
        return res;
    }
};
#endif