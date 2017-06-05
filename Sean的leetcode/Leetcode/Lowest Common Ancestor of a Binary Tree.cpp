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


    /* if the problem only gives the "int" p_val, q_val instead of "TreeNode*", we need use "count" to record the lowest ancestor because there may be duplicated value in the tree.
    */
    TreeNode* LCA(TreeNode *root, int p_val, int q_val, int &count)
    {
        TreeNode *left, *right;
        int count_left, count_right;

        if (!root)
            return 0;

        if (root->val == p_val || root->val == q_val)
        {
            count = 1;
            return root;
        }

        left = LCA(root->left, p_val, q_val, count_left);
        right = LCA(root->right, p_val, q_val, count_right);

        if (count_left == 2)
            return left;
        if (count_right == 2)
            return right;
        if (left && right)
        {
            count = 2;
            return root;
        }

        count = 1;
        return left ? left : right;
    }

    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        TreeNode *left, *right;

        if (!root || root == p || root == q) return root;

        left = lowestCommonAncestor(root->left, p, q);
        right = lowestCommonAncestor(root->right, p, q);

        if (left && right)
            return root;
        return left ? left : right;
    }
};