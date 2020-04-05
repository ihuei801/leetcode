//https://leetcode.com/discuss/38899/easy-short-c-recursive-solution
//O(logN*logN) time: worst case, each time compute height needs O(logN), and need to do it on each level, that is O(logN) times.
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
    int countNodes(TreeNode* root) {
        int left_height = 0, right_height = 0;
        TreeNode *l = root, *r = root;

        if (!root) return 0;

        while (l)
        {
            left_height++;
            l = l->left;
        }

        while (r)
        {
            right_height++;
            r = r->right;
        }

        if (left_height == right_height)
            return pow(2, left_height) - 1;
        else
            return 1 + countNodes(root->left) + countNodes(root->right);
    }
};