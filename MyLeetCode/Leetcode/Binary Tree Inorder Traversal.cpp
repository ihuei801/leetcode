/**
 * Definition for binary tree
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

#if 1 //iterative solution: Morris traversal
//Morris Traversal
class Solution {
public:
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int>res;
        TreeNode *curr = root;

        while (curr)
        {
            if (curr->left)
            {
                TreeNode *p = curr->left;
                while(p->right && p->right != curr)
                    p = p->right;

                if (!p->right)
                {
                    p->right = curr;
                    curr = curr->left;
                }
                else
                {
                    p->right = 0;
                    res.push_back(curr->val);
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
#else //recursive solution
class Solution {
public:

    vector<int> inorderTraversal(TreeNode *root) {
        vector<int>left, right;

        //if root is NULL, return empty vector.
        if (!root)
            return left;
        left = inorderTraversal(root->left);
        left.push_back(root->val);
        right = inorderTraversal(root->right);
        left.insert(left.end(), right.begin(), right.end());
        return left;
    }
};