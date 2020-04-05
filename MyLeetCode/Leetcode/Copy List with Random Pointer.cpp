#if 1 //Space: O(1)
//https://leetcode.com/discuss/22421/solution-constant-space-complexity-linear-time-complexity
/**
 * Definition for singly-linked list with a random pointer.
 * struct RandomListNode {
 *     int label;
 *     RandomListNode *next, *random;
 *     RandomListNode(int x) : label(x), next(NULL), random(NULL) {}
 * };
 */
class Solution {
public:
    RandomListNode *copyRandomList(RandomListNode *head) {
        RandomListNode *curr = head;
        RandomListNode *next, *dup, *tail;
        RandomListNode *dummy = new RandomListNode(0);

        if (!head) return 0;

        //generate duplicate node
        while (curr)
        {
            next = curr->next;
            curr->next = new RandomListNode(curr->label);
            curr->next->next = next;
            curr = next;
        }

        //copy random pointer
        curr = head;
        while (curr)
        {
            dup = curr->next;
            if (curr->random)
                dup->random = curr->random->next;
            else
                dup->random = 0;
            curr = dup->next;
        }

        //extract duplicate code
        curr = head;
        tail = dummy;
        while (curr)
        {
            next = curr->next->next;
            tail->next = curr->next;
            tail = curr->next;
            curr->next = next;
            curr = next;
        }
        return dummy->next;
    }
};
#elif 1//Space: O(n)
/**
 * Definition for singly-linked list with a random pointer.
 * struct RandomListNode {
 *     int label;
 *     RandomListNode *next, *random;
 *     RandomListNode(int x) : label(x), next(NULL), random(NULL) {}
 * };
 */
class Solution {
public:
    RandomListNode *copyRandomList(RandomListNode *head) {

        if (!head) return 0;

        unordered_map<RandomListNode *, RandomListNode *> n_map;
        RandomListNode *curr = head;

        while(curr)
        {
            RandomListNode *new_node;
            if (!n_map.count(curr))
                n_map[curr] = new RandomListNode(curr->label);
            new_node = n_map[curr];

            if (curr->next)
            {
                if (!n_map.count(curr->next))
                    n_map[curr->next] = new RandomListNode(curr->next->label);
                new_node->next = n_map[curr->next];
            }
            if (curr->random)
            {
                if (!n_map.count(curr->random))
                    n_map[curr->random] = new RandomListNode(curr->random->label);
                new_node->random = n_map[curr->random];
            }
            curr = curr->next;
        }
        return n_map[head];
    }
};
#endif