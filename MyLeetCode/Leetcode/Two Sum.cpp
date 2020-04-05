/*
HashTable
*/
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> table;
        vector<int> sol;
        if(nums.size() < 2) return sol;
        for(int i = 0; i < nums.size(); i++){
            if(table.count(target-nums[i])){
                sol.push_back(table[target-nums[i]]);
                sol.push_back(i);
                return sol;
            }
            table[nums[i]] = i;
        }
        return sol;
        
    }
};
#if 1// two pointer solution: use a vector<Node> elements to store index information.
class Solution {
public:

     struct Node  
     {  
            int val;  
            int index;      
            Node(int pVal, int pIndex):val(pVal), index(pIndex){}  
    };
    
    static bool compare(const Node &left, const Node &right)  
    {  
        return left.val < right.val;  
    }  
    
    vector<int> twoSum(vector<int> &numbers, int target) {
        vector<int>res;
        vector<Node> elements;  
        
        if (numbers.size() < 2) return res;
        
        
        for(int i =0; i< numbers.size(); i++)  
        {  
             elements.push_back(Node(numbers[i], i));  
        }  
        
        sort(elements.begin(), elements.end(), compare);  
        
        for (int i = 0, j = numbers.size()-1; i < j;)
        {
            int sum = elements[i].val + elements[j].val;     
            if (sum == target)
            {
                if (elements[i].index < elements[j].index)
                {
                    res.push_back(elements[i].index+1);
                    res.push_back(elements[j].index+1);                
                }
                else
                {
                    res.push_back(elements[j].index+1);
                    res.push_back(elements[i].index+1);                
                }
                break;
            }
            else if (sum < target)
                i++;
            else
                j--;
        }
        return res;
    }
};
#else //hash map solution
#include <map>
class Solution {
public:
    vector<int> twoSum(vector<int> &numbers, int target) {
        
        map<int, int>hash_table;
        int i;
        vector<int>res;
        
        res.clear();
        
        for (i = 0; i < numbers.size(); i++)
            hash_table[numbers[i]] = i;
            
        for (i = 0; i < numbers.size(); i++)                        
        {
            int diff = target - numbers[i];
            if (hash_table.find(diff) != hash_table.end() && hash_table[diff] != i)
            {
                res.push_back(i+1);
                res.push_back(hash_table[diff]+1);
                break;
            }
        }
        return res;
    }
};