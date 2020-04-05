#if 1
//advanced solution: http://jane4532.blogspot.tw/2013/07/flatten-binary-tree-to-linked.html
//tmp is the root node after build()
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
    void gen(TreeNode *root, TreeNode *&tmp)
    {
        if (root)
        {
            gen(root->right, tmp);
            gen(root->left, tmp);
            root->left = 0;
            root->right = tmp;
            tmp = root;
        }
    }
    void flatten(TreeNode* root) {
        TreeNode *tmp = 0;
        gen(root, tmp);
    }
};
#elif 1
//https://leetcode.com/discuss/637/can-you-improve-upon-my-recursive-approach
//iterative solution.
class Solution {
public:
    void flatten(TreeNode* root) {
        TreeNode *curr = root;
        while (curr)
        {
            if (curr->left)
            {
                TreeNode *p = curr->left;
                //to find the largest node in left subtree.
                while (p->right)
                    p = p->right;
                p->right = curr->right;
                curr->right = curr->left;
                curr->left = 0;
            }
            curr = curr->right;
        }
    }
};
#else
class Solution {
public:
    TreeNode* genFlatten(TreeNode *root, TreeNode *&tail)
    {
        TreeNode *left, *right, *left_tail, *right_tail;
        tail = 0;
        if (!root) return 0;

        left = genFlatten(root->left, left_tail);
        right = genFlatten(root->right, right_tail);

        if (!left && !right)
            tail = root;
        else
        {
            if (left)
            {
                left_tail->right = right;
                root->right = left;
                root->left = 0;
            }
            if (right_tail)
                tail = right_tail;
            else
                tail = left_tail;
        }
        return root;
    }
    void flatten(TreeNode* root) {
        TreeNode *tail;
        root = genFlatten(root, tail);
    }
};
#endif