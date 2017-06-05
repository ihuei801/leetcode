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
    ListNode* insertionSortList(ListNode* head) {
        ListNode *curr = head;
        //dummy->next is the actual new_head
        ListNode *dummy = new ListNode(0);
        ListNode *pivot = dummy;

        while (curr)
        {
            ListNode *next = curr->next;

            while (pivot->next && curr->val > pivot->next->val)
                pivot = pivot->next;

            curr->next = pivot->next;
            pivot->next = curr;

            pivot = dummy;
            curr = next;
        }
        return dummy->next;
    }
};