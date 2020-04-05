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
    ListNode *deleteDuplicates(ListNode *head) {
        ListNode *pivot = NULL, *curr = head;

        while (curr)
        {
            if (!pivot)
                pivot = curr;
            else if (pivot->val != curr->val)
            {
                pivot->next = curr;
                pivot = curr;
            }
            else //pivot->val == curr->val
                pivot->next = NULL;

            curr = curr->next;
        }
        return head;
    }
};