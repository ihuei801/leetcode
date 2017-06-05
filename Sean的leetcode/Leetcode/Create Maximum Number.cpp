/* DP, greedy
 * maxNumberLimit: find the max number of a limited length, keep the order decreasing, pop the last element if smaller
 * merge: merge two vectors to form a max number
 * greater: compare two vector of number
 */

class Solution {
public:
    vector<int> maxNumber(vector<int>& nums1, vector<int>& nums2, int k) {
        vector<int> greatest;
        int n = nums1.size();
        int m = nums2.size();
        for (int l1 = max(0, k - m); l1 <= min(n, k); l1++) {
            greatest = greater(greatest, merge(maxNumberLimit(nums1, l1), maxNumberLimit(nums2, k - l1)));
        }
        return greatest;
    }
    vector<int> maxNumberLimit(vector<int>& nums, int l) {
        int drop = nums.size() - l;
        vector<int> res;
        for (auto num : nums) {
            while (drop && !res.empty() && res.back() < num) {
                res.pop_back();
                drop--;
            }
            res.push_back(num);
        }
        res.resize(l)
        return res;
    }
    vector<int> merge(vector<int> nums1, vector<int> nums2) {
        int n = nums1.size();
        int m = nums2.size();
        int i = 0, j = 0;
        vector<int> res;
        while (i < n || j < m) {
            if (i == n) {
                res.push_back(nums2[j++]);
            }
            else if (j == m) {
                res.push_back(nums1[i++]);
            }
            else {
                if (nums1[i] == nums2[j]) {
                    int k = i, l = j;
                    while (k < n && l < m && nums1[k] == nums2[l]) {
                        k++;
                        l++;
                    }
                    if (l == m || k < n && nums1[k] > nums2[l]) {
                        res.push_back(nums1[i++]);
                    }
                    else {
                        res.push_back(nums2[j++]);
                    }
                }
                else if (nums1[i] > nums2[j]) {
                    res.push_back(nums1[i++]);
                }
                else {
                    res.push_back(nums2[j++]);
                }
            }
        }
        return res;
        
    }
    vector<int> greater(vector<int> nums1, vector<int> nums2) {
        int n = nums1.size();
        int m = nums2.size();
        if (n != m) return n > m? nums1 : nums2;
        int i = 0;
        while (i < n) {
            if (nums1[i] != nums2[i]) {
                return nums1[i] > nums2[i]? nums1 : nums2;
            }
            i++;
        }
        return nums1;
    }
};