class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        vector<vector<int>> res;
        for (int i = 0; i < nums.size(); i++) {
            // skip duplicates
            if (i > 0 && nums[i] == nums[i-1]) {
                continue;
            }
            // sorted 2 sum
            int l = i + 1;
            int r = nums.size()-1;
            // cant reuse same value in the triplet => all 3 distinct
            while (l < r) {
                int sum = nums[i] + nums[l] + nums[r];
                if (sum == 0) {
                    vector<int> cur = {nums[i], nums[l], nums[r]};
                    res.push_back(cur);
                    l++;
                    r--;
                    while (l<r and nums[l] == nums[l-1]) {
                        l++;
                    }
                } else if (sum > 0) {
                    r--;
                } else {
                    l++;
                }
            }
        }
        return res;
    }
};
