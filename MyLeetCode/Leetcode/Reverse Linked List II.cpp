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
    ListNode* reverseBetween(ListNode* head, int m, int n) {
        ListNode *pre_tail = 0;
        ListNode *r_head = head;

        for (int i = 0; i < m-1; i++)
        {
            pre_tail = r_head;
            r_head = r_head->next;
        }

        ListNode *curr = r_head;
        ListNode *pre = 0;
        for (int i = 0; i < n-m+1; i++)
        {
            ListNode *next = curr->next;
            curr->next = pre;
            pre = curr;
            curr = next;
        }
        r_head->next = curr;
        if (pre_tail)
        {
            pre_tail->next = pre;
            return head;
        }
        else
            return pre;
    }
};