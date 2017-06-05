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
    TreeNode *build(vector<int>& inorder, int in_start, int in_end, vector<int>& postorder, int post_start, int post_end)
    {
        int i;
        if (in_start > in_end) return 0;

        TreeNode *root = new TreeNode(postorder[post_end]);

        for (i = in_start; i <= in_end; i++)
            if (inorder[i] == root->val)
                break;

        int left_num = i - in_start;
        root->left = build(inorder, in_start, i-1, postorder, post_start, post_start+left_num-1);
        root->right = build(inorder, i+1, in_end, postorder, post_start+left_num, post_end-1);
        return root;
    }

    TreeNode* buildTree(vector<int>& inorder, vector<int>& postorder) {
        return build(inorder, 0, inorder.size()-1, postorder, 0, postorder.size()-1);
    }
};
