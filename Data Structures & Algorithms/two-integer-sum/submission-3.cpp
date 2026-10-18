class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        map<int, int> numToIndex;
        for (int i = 0; i < nums.size(); i++){
            int num = nums[i];
            int diff = target - num;
            if (numToIndex.contains(diff)) {
                // {} is used to initialize containers
                vector<int> res = {numToIndex[diff], i};
                return res;
            }
            numToIndex[num] = i;
        }
    }
};
