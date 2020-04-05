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

    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode *head, *tail;

        head = tail = 0;
        int carry = 0;
        while (l1 || l2 || carry)
        {
            int sum = 0;

            sum += l1 ? l1->val : 0;
            sum += l2 ? l2->val : 0;
            l1 = l1 ? l1->next : 0;
            l2 = l2 ? l2->next : 0;

            sum += carry;
            carry = sum / 10;
            ListNode *n = new ListNode(sum%10);

            if (!tail)
                head = tail = n;
            else
            {
                tail->next = n;
                tail = n;
            }
        }
        return head;
    }
};