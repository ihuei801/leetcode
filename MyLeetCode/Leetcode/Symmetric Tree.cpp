/**
 * Definition for binary tree
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    bool isSymmetricTree(TreeNode *left_root, TreeNode *right_root)
    {
        if (!left_root && !right_root)
            return true;

        if (!left_root || !right_root)
            return false;

        if (left_root->val == right_root->val
            && isSymmetricTree(left_root->left, right_root->right)
            && isSymmetricTree(right_root->left, left_root->right))
            return true;


        return false;
    }

    bool isSymmetric(TreeNode *root) {

        if (!root) return true;
        else
            return isSymmetricTree(root->left, root->right);
    }
};