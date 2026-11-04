class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> seen;
        for (int i = 0; i < nums.size(); i++) {
            int cur = nums[i];
            int diff = target - cur;
            if (seen.contains(diff)) {
                vector<int> res;
                res.push_back(seen[diff]);
                res.push_back(i);
                return res;
            }
            seen[cur] = i;
        }
    }
};
