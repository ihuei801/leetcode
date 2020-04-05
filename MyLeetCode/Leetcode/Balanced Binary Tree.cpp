/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
//Time: O(N)
class Solution {
public:
    //return -1: not balanced. otherwise: the depth
    int depth(TreeNode *root)
    {
        if (!root) return 0;

        int left_depth = depth(root->left);
        int right_depth = depth(root->right);

        if (left_depth < 0 || right_depth < 0 || (abs(left_depth - right_depth) > 1))
            return -1;

        return max(left_depth, right_depth) + 1;
    }
    bool isBalanced(TreeNode* root) {
        return depth(root) >= 0;
    }
};