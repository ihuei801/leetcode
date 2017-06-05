/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    void deleteNode(ListNode* node) {
#if 1
        ListNode *next = node->next;
        *node = *next;
        free(next);
#else
        if (!node)
            return;
        ListNode *next = node->next;
        if (next)
        {
            node->val = next->val;
            node->next = next->next;
            free(next);
        }
    }
#endif
};