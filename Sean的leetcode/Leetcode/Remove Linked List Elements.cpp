#if 1 //recursive solution
class Solution {
public:
    ListNode* removeElements(ListNode* head, int val) {
        ListNode *new_head;
        if (!head) return head;

        new_head = removeElements(head->next, val);

        if (head->val == val)
            return new_head;
        else
        {
            head->next = new_head;
            return head;
        }
    }
};
#else //iterative solution
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
    ListNode* removeElements(ListNode* head, int val) {
        ListNode *curr, *next, *pre = 0;
        curr = head;

        while (curr)
        {
            next = curr->next;
            if (curr->val == val)
            {
                if (pre)
                    pre->next = next;
                else
                    head = next;

                free(curr);
            }
            else
                pre = curr;

            curr = next;
        }
        return head;
    }
};
#endif