//refer to the solution of : http://www.cnblogs.com/hiddenfox/p/3408931.html
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
    ListNode *detectCycle(ListNode *head) {
        ListNode *slow = head, *fast = head;
        ListNode *curr;

        if (!head) return 0;

        while (slow && fast)
        {
            slow = slow->next;
            if (fast->next)
                fast = fast->next->next;
            else
                return 0;

            if (slow == fast)
                break;
        }

        if (!slow || !fast)
            return 0;

        //the distance between the head and cycle beginning is the same as
        //the distance between the meeting point and the cycle beginning :  a: head to loop start, b: loop start to meeting point, x: meeting point to loop start,slow: a+b, fast: a+b+x+b = 2(a+b) => x = a
        curr = head;
        while (curr != slow)
        {
            curr = curr->next;
            slow = slow->next;
        }
        return curr;
    }
};