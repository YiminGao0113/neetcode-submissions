#include <unordered_map>

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> seen;
        int i = 0;
        for (auto num : nums){
            int sub = target - num;
            if (seen.count(sub)){
                return {seen[sub], i};
            }
            seen[num] = i;
            i++;
        }
    }
};
