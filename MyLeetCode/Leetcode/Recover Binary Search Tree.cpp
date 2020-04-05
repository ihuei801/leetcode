/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
#if 1//Morris Traversal, Space: O(1), Time: O(N)
class Solution {
public:

    void checkError(TreeNode *&small, TreeNode *&large, TreeNode *&pre, TreeNode *curr)
    {
        if (pre && pre->val >= curr->val)
        {
            if (!large)
            {
                large = pre;
                small = curr;
            }
            else
                small = curr;
        }
        pre = curr;
    }

    void recoverTree(TreeNode* root) {
        TreeNode *small, *large, *pre;
        TreeNode *curr = root;
        small = large = pre = 0;

        while (curr)
        {
            if (curr->left)
            {
                TreeNode *temp = curr->left;
                while (temp->right && temp->right != curr)
                    temp = temp->right;

                if (!temp->right)
                {
                    temp->right = curr;
                    curr = curr->left;
                }
                else
                {
                    //print curr
                    temp->right = 0;
                    checkError(small, large, pre, curr);
                    curr = curr->right;
                }
            }
            else
            {
                //print curr
                checkError(small, large, pre, curr);
                curr = curr->right;
            }
        }
        swap(small->val, large->val);
    }
};
#else //recursive solution, Space: O(logN), Time: O(N)
class Solution {
public:

    void inorder(TreeNode *root, TreeNode *&small, TreeNode *&large, TreeNode *&pre)
    {
        if (!root) return;

        inorder(root->left, small, large, pre);

        if (pre && pre->val >= root->val)
        {
            if (!large)
            {
                large = pre;
                small = root;
            }
            else
                small = root;
        }

        pre = root;
        inorder(root->right, small, large, pre);
    }

    //user inorder to check BST validity.
    void recoverTree(TreeNode* root) {
        TreeNode *small, *large, *pre;

        small = large = pre = 0;
        inorder(root, small, large, pre);
        swap(small->val, large->val);
    }
};
#endif