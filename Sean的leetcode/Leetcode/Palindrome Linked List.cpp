//https://leetcode.com/discuss/44733/c-o-n-time-o-1-space-solution
//reverse the 2nd half list then compare with the 1st half list.
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
    ListNode *reverse(ListNode *head)
    {
        ListNode *pre = 0;
        ListNode *curr = head;

        while (curr)
        {
            ListNode *next = curr->next;
            curr->next = pre;
            pre = curr;
            curr = next;
        }
        return pre;
    }

    bool isPalindrome(ListNode* head) {
        ListNode *curr = head;
        ListNode *mid;
        int num = 0;

        if (!head) return true;

        while (curr)
        {
            num++;
            curr = curr->next;
        }

        curr = head;
        for (int i = 0; i < num >> 1; i++)
            curr = curr->next;

        mid = reverse(curr);
        curr = head;
        while (mid)
        {
            if (mid->val != curr->val)
                return false;
            mid = mid->next;
            curr = curr->next;
        }
        return true;
    }
};