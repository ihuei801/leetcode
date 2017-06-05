#if 1
/**
 * Definition for binary tree
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

//When BST is inorder sequence, it should be an ascending sequence.
class Solution {
public:
    bool verifyBST(TreeNode *root, TreeNode *&pre_node)
    {
        if (!root) return true;

        if (!verifyBST(root->left, pre_node))
            return false;

        if (pre_node && pre_node->val >= root->val)
            return false;

	    //pre_node is update to the previous node in inorder sequence of the next checking node.
        pre_node = root;

        if (!verifyBST(root->right, pre_node))
            return false;

        return true;
    }

    bool isValidBST(TreeNode *root) {
        TreeNode *pre_node = 0;
        return verifyBST(root, pre_node);
    }
};
#elif 1 //[min, max] range
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
    bool verify(TreeNode *root, TreeNode *min_t, TreeNode *max_t)
    {
        if (!root) return true;

        if (!verify(root->left, min_t, root))
            return false;

        if ((min_t && root->val <= min_t->val) || (max_t && root->val >= max_t->val))
            return false;

        return verify(root->right, root, max_t);
    }

    bool isValidBST(TreeNode* root) {
        return verify(root, 0, 0);
    }
};
#endif