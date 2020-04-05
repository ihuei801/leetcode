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
    TreeNode* invertTree(TreeNode* root) {
        TreeNode *right, *left;
        if (!root)
            return NULL;

        right = invertTree(root->right);
        left = invertTree(root->left);
        root->left = right;
        root->right = left;
        return root;
    }
};