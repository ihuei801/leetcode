//https://leetcode.com/discuss/21032/very-concise-one-pass-solution
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
    ListNode* partition(ListNode* head, int x) {
        //small list
        ListNode *p1 = new ListNode(0);
        //larger list
        ListNode *p2 = new ListNode(0);

        ListNode *p1_tail = p1;
        ListNode *p2_tail = p2;

        ListNode *curr = head;
        while (curr)
        {
            if (curr->val < x)
            {
                p1_tail->next = curr;
                p1_tail = curr;
            }
            else
            {
                p2_tail->next = curr;
                p2_tail = curr;
            }
            curr = curr->next;
        }
        p1_tail->next = p2->next;
        p2_tail->next = 0;
        return p1->next;
    }
};