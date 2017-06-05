class Solution {
public:
    ListNode *removeNthFromEnd(ListNode *head, int n) {
            
            ListNode *target = head, *p = head, *pre = NULL;
            
            for (int i = 0; i < n; i++)
                p = p->next;
                
            while (p)
            {
                pre = target;
                target = target->next;
                p = p->next;
            }
            
            if (target)
            {
                if (pre)
                    pre->next = target->next;
                else
                    head = target->next;
                                
            }
            return head;                
    }
};