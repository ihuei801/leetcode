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
    int maxDepth(TreeNode* root) {
        int left, right;

        if (!root) return 0;

        left = maxDepth(root->left);
        right = maxDepth(root->right);
        return max(left, right) + 1;
    }
};