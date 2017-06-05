//http://www.geeksforgeeks.org/longest-monotonically-increasing-subsequence-size-n-log-n/
//array keep track of the smallest end element of a sequence with len = i+1 
//Time: O(NlogN)
class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        int size = nums.size();
        vector<int> lst;
        for (int e: nums) {
            if ( lst.empty() ) {
                lst.push_back(e);
            } 
            else if (e < lst[0]) {
                lst[0] = e;
            } 
            else if (e > lst.back()) {
                lst.push_back(e);
            } 
            else {
                int l = 0;
                int r = lst.size() - 1;
                while (l + 1 < r) {
                    int mid = l + (r - l) / 2;
                    if (lst[mid] >= e) {
                        r = mid;
                    } else {
                        l = mid;
                    }
                    
                }
                if (lst[l] >= e) {
                    lst[l] = e;
                } 
                else {
                    lst[r] = e;
                }
                
            }
        }
        return lst.size();
    }
};

//Sean
class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        int n = nums.size();

        vector<int> lis;

        for (auto a : nums)
        {
            if (lis.empty())
                lis.push_back(a);
            else if (a < lis[0])
                lis[0] = a;
            else if (a > lis.back())
                lis.push_back(a);
            else
            {
                int left = 0;
                int right = lis.size()-1;
                while (left <= right)
                {
                    int mid = left + ((right - left) >> 1);
                    //note: this should be ">=" to overwrite lis[mid] equal to a.
                    if (lis[mid] >= a)
                        right = mid - 1;
                    else
                        left = mid + 1;
                }
                lis[left] = a;
            }
        }
        return lis.size();
    }
};