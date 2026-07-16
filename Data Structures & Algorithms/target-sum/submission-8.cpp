class Solution {
public:
    int findTargetSumWays(vector<int>& nums, int target) {
        int totalSum = 0;
        for (int i = 0; i < nums.size(); i++ ) {
            totalSum += nums[i];
        }
        if (target > totalSum || target < -totalSum) {
            return 0;
        }
        vector<vector<int>> dp;
        dp.resize(nums.size()+1);
        std::cout << dp.size();
        for (int i = 0; i < nums.size()+1; i++){
            dp[i].resize(2 * totalSum + 1, 0);
        }
        std::cout << dp[0].size();
        int offset = totalSum;
        dp[nums.size()][target + offset] = 1;
        for (int i = nums.size()-1; i >= 0; i--){
            for (int j = totalSum + offset; j >= 0; j--){
                int add = 0;
                if (j + nums[i] < dp[0].size()) {
                    add = dp[i+1][j+nums[i]];
                }
                int substract = 0;
                if (j - nums[i] >= 0) {
                    substract = dp[i+1][j - nums[i]];
                }
                dp[i][j] = add + substract;
            }
        }
        return dp[0][0 + offset];
    }
};
