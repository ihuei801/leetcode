/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
//Time: O(n)
//Space: O(logN) because of the stack of recursive call.
class Solution {
public:
    TreeNode* build(ListNode *&head, int start, int end)
    {
        if (start > end) return 0;

        int mid = (start + end) >> 1;

        TreeNode *left = build(head, start, mid-1);
        TreeNode *root = new TreeNode(head->val);
        head = head->next;
        TreeNode *right = build(head, mid+1, end);
        root->left = left;
        root->right = right;
        return root;
    }

    TreeNode* sortedListToBST(ListNode* head) {
        int num = 0;
        ListNode *curr;
        for (curr = head; curr; curr = curr->next)
            num++;
        return build(head, 0, num-1);
    }
};