#if //iterative solution
//https://leetcode.com/discuss/54438/4-7-lines-recursive-iterative-ruby-c-java-python
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
//Time: O(logN)
class Solution {
public:
    int closestValue(TreeNode* root, double target) {
        if (!root) return INT_MIN;
        int close = root->val;
        TreeNode* curr = root;
        while (curr) {
            if (curr->val == target) return target;
            else if (abs(curr->val - target) < abs(close - target)) {
                close = curr->val;
            }
            curr = target <= curr->val? curr->left : curr->right;
        }
        return close;
    }
};
#elif 1 //recursive solution
//https://leetcode.com/discuss/54438/4-7-lines-recursive-iterative-ruby-c-java-python
class Solution {
public:
    int closestValue(TreeNode* root, double target) {
        if (!root) return INT_MAX;

        TreeNode *child = root->val < target ? root->right : root->left;

        if (!child) return root->val;

        int c_val = closestValue(child, target);
        return abs(root->val - target) < abs(c_val - target) ? root->val : c_val;
    }
};
#endif;