/*Reservoir Sampling
https://discuss.leetcode.com/topic/53753/brief-explanation-for-reservoir-sampling/2
Time Complexity: O(n)
Space Complexity: O(1)
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
    /** @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node. */
    Solution(ListNode* head) {
        list = head;
    }
    
    /** Returns a random node's value. */
    int getRandom() {
        int num = 2;
        int re = list->val;
        ListNode* node = list->next;
        while (node) {
            int randnum = rand() % num;
            if (randnum == 0) {
                re = node->val;
            }
            num++;
            node = node->next;
        }
        return re;
    }
private:
    ListNode* list;
};

/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = new Solution(head);
 * int param_1 = obj.getRandom();
 */