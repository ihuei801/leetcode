//Two Pointers: one to traverse and the other keep the right-most node that is not 9
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
    ListNode* plusOne(ListNode* head) {
        ListNode* newhead = new ListNode(0);
        newhead->next = head;
        ListNode* ptr = newhead;
        ListNode* curr = newhead;
        while (curr) {
            if (curr->val != 9) {
                ptr = curr;
            }
            curr = curr->next;
        }
        ptr->val++;
        curr = ptr->next;
        while (curr) {
            curr->val = 0;
            curr = curr->next;
        }
        return newhead->val == 0? newhead->next : newhead;
    }
};
//Sean's solution
//Time complexity:O(n)
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
    ListNode* plusOne(ListNode* head) {
        ListNode* newhead = new ListNode(0);
        newhead->next = head;
        ListNode* i = newhead, *j = newhead;
        for (i = newhead; i->next != NULL; i = i->next) {
            if (i->val != 9) {
                j = i;
            }
        }
        if (i->val != 9) {
            i->val += 1;
            return head;
        }
        j->val += 1;
        for (j = j->next; j != NULL; j = j->next) {
            j->val = 0;
        }
        if (newhead->val != 0) return newhead;
        else return head;
    }
};