#if 1//iterative solution
//http://www.careercup.com/question?id=6266917077647360
//https://leetcode.com/discuss/27499/2ms-solution-with-c
//use careercup link to understand the step:
//current->left = parent->right
//current->right = parent
class Solution {
public:
    TreeNode *upsideDownBinaryTree(TreeNode *root){
        TreeNode *parent = 0, *parent_right = 0, *next;
        TreeNode *curr = root;
        //use the concept of reverse linked list.
        while (curr)
        {
            next = curr->left;
            curr->left = parent_right;
            parent_right = curr->right;
            //note: the sequence cannot change, otherwise curr->right is overwritten.
            curr->right = parent;
            parent = curr;
            curr = next;
        }
        return parent;
    }
};
#elif //recursive solution
//https://leetcode.com/problems/binary-tree-upside-down/
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
    TreeNode* upsideDownBinaryTree(TreeNode* root) {
        if (!root || !root->left) return root;
        TreeNode *new_root = upsideDownBinaryTree(root->left);
        root->left->right = root;
        root->left->left = root->right;
        root->left = root->right = 0;
        return new_root;
    }
};
#endif