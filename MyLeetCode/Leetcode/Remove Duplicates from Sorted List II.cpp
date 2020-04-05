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
    ListNode* deleteDuplicates(ListNode* head) {
        ListNode *new_head = 0;
        ListNode *tail = 0;
        ListNode *pre = 0;
        ListNode *curr = head;

        while (curr)
        {
            ListNode *next = curr->next;

            //if the curr is different from pre and next node, add curr into the result.
            if ((!pre || pre->val != curr->val)
                && (!next || next->val != curr->val))
            {
                if (!new_head)
                    new_head = tail = curr;
                else
                {
                    tail->next = curr;
                    tail = curr;
                }
                tail->next = 0;
            }
            pre = curr;
            curr = next;
        }
        return new_head;
    }
};