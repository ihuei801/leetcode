#if 1 //full recursive solution
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
//O(logN) space (recursive stack size)
class Solution {
public:

    ListNode *merge(ListNode *first, ListNode *sec)
    {
        ListNode *head = NULL;
        ListNode *next;
        if (!first)
            return sec;
        if (!sec)
            return first;

        if (first->val < sec->val)
        {
            head = first;
            first = first->next;
        }
        else
        {
            head = sec;
            sec = sec->next;
        }

        next = merge(first, sec);
        head->next = next;
        return head;
    }

    ListNode *mergeSort(ListNode *&curr, int num)
    {
        ListNode *left, *right;

        if (num == 0)
            return NULL;
        if (num == 1)
        {
            ListNode *old_curr = curr;
            curr = curr->next;
            old_curr->next = NULL;
            return old_curr;
        }

        left = mergeSort(curr, num/2);
        right = mergeSort(curr, num-num/2);
        return merge(left, right);
    }

    ListNode *sortList(ListNode *head) {
        int num = 0;
        ListNode *curr = head;
        while (curr)
        {
            num++;
            curr = curr->next;
        }
        return mergeSort(head, num);
    }
};
#else //partial recursive solution
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
 //use merge sort to reach O(nlogn)
class Solution {
public:

    ListNode *merge(ListNode *first, ListNode *sec)
    {
        ListNode *head = NULL, *tail = NULL;
        ListNode *min;

        if (!first) return sec;
        if (!sec)   return first;

        while (first || sec)
        {
            if (first && sec)
                min = (first->val > sec->val) ? (sec) : (first);
            else if (!first)
                min = sec;
            else if (!sec)
                min = first;

            if (!tail)
                head = tail = min;
            else
            {
                tail->next = min;
                tail = min;
            }

            if (min == first)
                first = first->next;
            else if (min == sec)
                sec = sec->next;
        }
        return head;
    }

    ListNode *mergeSort(ListNode **head, int num)
    {
        ListNode *left, *right;

        if (num == 0)
            return NULL;
        //if only one node exists, return the current head node and set head->next as NULL.
        if (num == 1)
        {
            ListNode *old_head = (*head);
            //Important: we should make sure that head will advance. otherwise head will always the first element.
            (*head) = (*head)->next;
            old_head->next = NULL;
            return old_head;
        }

        left = mergeSort(head, num/2);
        right = mergeSort(head, num - num/2);
        return merge(left, right);
    }

    ListNode *sortList(ListNode *head) {

        int num = 0;
        ListNode *p = head;

        while (p)
        {
            num++;
            p = p->next;
        }
        return mergeSort(&head, num);
    }
};