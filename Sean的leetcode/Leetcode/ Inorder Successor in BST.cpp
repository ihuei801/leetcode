/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
//Time: O(h), h is tree height.
class Solution {
public:
    TreeNode* inorderSuccessor(TreeNode* root, TreeNode* p) {
        if (!root || !p) return 0;

        TreeNode *curr = root, *succ;
        while (curr)
        {
            if (curr->val == p->val)
                curr = curr->right;
            else if (curr->val > p->val)
            {
                succ = curr;
                curr = curr->left;
            }
            else
                curr = curr->right;
        }
        return succ;
    }
};