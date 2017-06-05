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
    ListNode *rotateRight(ListNode *head, int k) {
        
        ListNode *pre_target = 0, *target = 0;
        ListNode *tail = 0, *temp = head;
        int num = 0;
        int i;
        
        if (!head) return head;
        
        //find total number
        while (temp)
        {
            num++;
            tail = temp;
            temp = temp->next;
        }
        
        k %= num;
        
        if (k == 0) return head;
        
        //find new head (target)
        for (i = 0, target = head; i < num - k; i++)
        {
            pre_target = target;
            target     = target->next;
        }
        
        pre_target->next = NULL;
        tail->next = head;
            
        return target;
    }
};