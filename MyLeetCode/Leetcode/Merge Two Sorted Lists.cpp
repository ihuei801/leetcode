/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
 #if 1
class Solution {
public:
    ListNode *mergeTwoLists(ListNode *l1, ListNode *l2) {
        ListNode *head = NULL;
        ListNode *tail = NULL;

        if (!l1) return l2;
        if (!l2) return l1;

        while (l1 && l2)
        {
            ListNode *min_node;
            min_node = (l1->val < l2->val) ? (l1) : (l2);

            if (!head)
                head = tail = min_node;
            else
            {
                tail->next = min_node;
                tail = min_node;
            }

            if (l1 == min_node)
                l1 = l1->next;
            else
                l2 = l2->next;

            tail->next = NULL;
        }

        if (l1)
            tail->next = l1;
        if (l2)
            tail->next = l2;
        return head;
    }
};
#else //recrusvie solution
class Solution {
public:
    ListNode *mergeTwoLists(ListNode *l1, ListNode *l2) {

        ListNode *head;
        if (!l1)
            return l2;
        if (!l2)
            return l1;

        if (l1->val < l2->val)
        {
            head = l1;
            l1 = l1->next;
        }
        else
        {
            head = l2;
            l2 = l2->next;
        }
        head->next = mergeTwoLists(l1, l2);
        return head;
    }
};
#endif