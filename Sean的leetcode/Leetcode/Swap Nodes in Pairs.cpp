#if 1
//iterative version, skip 2 nodes in every iteration.
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
    ListNode* swapPairs(ListNode* head) {
        ListNode *new_head = 0, *new_tail = 0;
        ListNode *curr = head, *next, *next2;

        if (!head || !head->next) return head;

        while (curr && curr->next)
        {
            next  = curr->next;
            next2 = curr->next->next;

            curr->next = next->next;
            next->next = curr;

            if (!new_head)
            {
                new_head = next;
                new_tail = curr;
            }
            else
            {
                new_tail->next = next;
                new_tail = curr;
            }
            curr = next2;
        }
        return new_head;
    }
};
#elif 1 //recursive version
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
    ListNode *swapPairs(ListNode *head) {
        ListNode *new_head, *next;

        if (!head || !head->next)
            return head;

        new_head = head->next;
        next     = new_head->next;
        new_head->next = head;
        head->next = swapPairs(next);
        return new_head;
    }
};
#endif