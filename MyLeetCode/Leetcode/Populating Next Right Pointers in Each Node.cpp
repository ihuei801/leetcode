#if 1 //recursive solution
/**
 * Definition for binary tree with next pointer.
 * struct TreeLinkNode {
 *  int val;
 *  TreeLinkNode *left, *right, *next;
 *  TreeLinkNode(int x) : val(x), left(NULL), right(NULL), next(NULL) {}
 * };
 */
class Solution {
public:
    void connect(TreeLinkNode *root) {

        if (!root)
            return;

        if (root->left && root->right)
        {
            root->left->next = root->right;

            if (root->next)
                root->right->next = root->next->left;
            else
                root->right->next = 0;

            connect(root->left);
            connect(root->right);
        }
    }
};
#elif 1 //iterative solution
/**
 * Definition for binary tree with next pointer.
 * struct TreeLinkNode {
 *  int val;
 *  TreeLinkNode *left, *right, *next;
 *  TreeLinkNode(int x) : val(x), left(NULL), right(NULL), next(NULL) {}
 * };
 */
class Solution {
public:
    void connect(TreeLinkNode *root) {
        if (!root) return;

        TreeLinkNode *next = 0;
        TreeLinkNode *pre = 0;
        TreeLinkNode *curr = root;

        while (curr)
        {
            if (!next)
                next = curr->left;
            if (pre)
                pre->next = curr->left;
            if (curr->left)
                curr->left->next = curr->right;

            pre = curr->right;
            curr = curr->next;
            if (!curr)
            {
                curr = next;
                next = pre = 0;
            }
        }
    }
};
#endif