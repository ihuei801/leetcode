//1. refer to http://jane4532.blogspot.tw/2013/07/populate-pointers-to-each-node.html
//2. use BFS concept.
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
        TreeLinkNode *curr = root, *next = 0;
        TreeLinkNode *pre = 0;

        while (curr)
        {
            for (; curr; curr = curr->next)
            {
                if (!curr->left && !curr->right)
                    continue;

                if (curr->left)
                    curr->left->next = curr->right;

                if (pre)
                    pre->next = curr->left ? curr->left : curr->right;

                if (curr->left || curr->right)
                    pre = curr->right ? curr->right : curr->left;

                if (!next)
                    next = curr->left ? curr->left : curr->right;
            }
            curr = next;
            next = pre = 0;
        }
    }
};