/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
//Time: O(NlongN): N + 2*(N/2) + 4*(N/4) + 8*(N/8) + ... 1 = N*longN
class Solution {
public:
    TreeNode* build(vector<int>& preorder, vector<int>& inorder, int pre_start, int pre_end, int in_start, int in_end)
    {
        TreeNode *root, *left, *right;
        int i;
        int left_num;

        if (pre_start > pre_end)
            return 0;

        root = new TreeNode(preorder[pre_start]);

        for (i = in_start; i <= in_end; i++)
            if (inorder[i] == preorder[pre_start])
                break;

        left_num = i - in_start;
        left = build(preorder, inorder, pre_start+1, pre_start+left_num, in_start, i-1);
        right = build(preorder, inorder, pre_start+left_num+1, pre_end, i+1, in_end);
        root->left = left;
        root->right = right;
        return root;
    }

    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        return build(preorder, inorder, 0, preorder.size()-1, 0, inorder.size()-1);
    }
};