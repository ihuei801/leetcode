//1. Break list in the middle to two lists (use fast & slow pointers)
//2. Reverse the order of the second list
//3. Merge two list back together

class Solution {
public:

    void reorderList(ListNode *head) {
        ListNode *fast = head, *slow = NULL;
        ListNode *first, *sec, *curr, *next;
        ListNode *pre = NULL;

        //break list in the middle into two lists
        while (1)
        {
            if (fast && fast->next)
            {
                fast = fast->next->next;

                if (!slow)
                    slow = head->next;
                else
                    slow = slow->next;
            }
            else
                break;
        }

        //node num less than 3.
        if (!slow)
            return;

        //curr is the head of the second list
        curr = slow->next;

        //separate 2 lists
        slow->next = NULL;

        //reverse the 2nd list
        while (curr)
        {
            next = curr->next;
            curr->next = pre;
            pre = curr;
            curr = next;
        }

        //merge 2 lists
        first = head;
        sec = pre;

        while(first && sec)
        {

            ListNode *temp;
            temp = sec->next;
            sec->next = first->next;
            first->next = sec;
            first = sec->next;
            sec = temp;
        }
    }
};