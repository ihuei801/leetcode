#if 1 //iterative solution
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
    ListNode* reverseKGroup(ListNode* head, int k) {
        ListNode *curr = head;
        int num = 0;

        while (curr)
        {
            num++;
            curr = curr->next;
        }

        //note: need early return.
        if (!head || num < k)
            return head;

        ListNode *next, *tail, *pre = 0, *pre_tail = 0;
        ListNode *new_head;
        curr = head;
        while (num >= k)
        {
            for (int i = 0; i < k; i++)
            {
                if (!pre)
                    tail = curr;
                next = curr->next;
                curr->next = pre;
                pre = curr;
                curr = next;
            }

            if (!pre_tail)
                new_head = pre;
            else
                pre_tail->next = pre;

            pre = 0;
            pre_tail = tail;
            num -= k;
        }
        pre_tail->next = curr;
        return new_head;
    }
};
#elif 1 //recursive solution
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
    ListNode* reverseKGroup(ListNode* head, int k) {
        ListNode *curr = head;
        int num = 0;

        while (curr)
        {
            num++;
            curr = curr->next;
        }

        //note: need early return.
        if (!head || num < k)
            return head;

        ListNode *next, *pre = 0;
        curr = head;
        for (int i = 0; i < k; i++)
        {
            next = curr->next;
            curr->next = pre;
            pre = curr;
            curr = next;
        }

        head->next = reverseKGroup(curr, k);
        return pre;
    }
};
#endif