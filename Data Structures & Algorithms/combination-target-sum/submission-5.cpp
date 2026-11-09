class Solution {
private:
    int target;
    vector<int> nums;
    vector<vector<int>> res;
    void dfs(int i, int total, vector<int>& combo){
        if (i >= nums.size() || total > target) {
            return;
        }
        // push back a copy of combo
        if (total == target) {
            res.push_back(combo);
            return;
        }

        // include and reuse nums[i]
        combo.push_back(nums[i]);
        dfs(i, total+nums[i], combo);

        // exclude nums[i]
        combo.pop_back();
        dfs(i+1, total, combo);

        return;
    }

public:
    vector<vector<int>> combinationSum(vector<int>& nums, int target) {
        this->target = target;
        this->nums = nums;
        vector<int> combo;
        dfs(0,0,combo);
        return res;
    }
};
