//priority_queue
//Time complexity:O(log(m+n))
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
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
    struct comp {
        bool operator()(ListNode* a, ListNode* b) {
            return a->val > b->val;
        }
    };
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        priority_queue<ListNode*, vector<ListNode*>, comp> pq;
        for (auto l : lists) {
            if (l) {
                pq.push(l);
            }
        }
        ListNode* newnode = new ListNode(0);
        ListNode* tail = newnode;
        while (!pq.empty()) {
            ListNode* tmp = pq.top();
            pq.pop();
            if (tmp->next) {
                pq.push(tmp->next);
            }
            tail->next = tmp;
            tail = tail->next;
        }
        return newnode->next;
    }
};

//Sean's Solution
#if 1 //priority_queue solution
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
    static bool compare(ListNode *a, ListNode *b)
    {
        //note: we should use ">" here because the output should be ascending order.
        return a->val > b->val;
    }

    ListNode* mergeKLists(vector<ListNode*>& lists) {
        ListNode *head = 0;
        ListNode *curr, *tail;
        priority_queue<ListNode*, vector<ListNode*>, function<bool(ListNode *, ListNode *)>> pq(compare);
        for (int i = 0; i < lists.size(); i++)
            for (curr = lists[i]; curr; curr = curr->next)
                pq.push(curr);

        while (pq.size())
        {
            if (head)
            {
                tail->next = pq.top();
                tail = tail->next;
            }
            else
                head = tail = pq.top();
            tail->next = 0;
            pq.pop();
        }
        return head;
    }
};
#else
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
 #define MIN(a, b) ((a < b) ? (a) : (b))
//compare the min node for every list in one iteration
class Solution {
public:
    ListNode *mergeKLists(vector<ListNode *> &lists) {

        int min_index = -1;
        ListNode *head = NULL, *tail = NULL, *next;
        int all_empty = 1;
        int i;

        if (lists.size() == 0)
            return NULL;

        while (1)
        {
            for (i = 0, min_index = -1, all_empty = 1; i < lists.size(); i++)
            {
                if (lists[i])
                    all_empty = 0;
                else
                    continue;

                if (min_index == -1)
                    min_index = i;
                else if (lists[i]->val < lists[min_index]->val)
                    min_index = i;
            }

            if (all_empty)
                break;

            next = lists[min_index]->next;

            if (!head)
                head = tail = lists[min_index];
            else
                tail->next = lists[min_index];

            tail = lists[min_index];
            tail->next = NULL;
            lists[min_index] = next;
        }
        return head;
    }
};
#endif