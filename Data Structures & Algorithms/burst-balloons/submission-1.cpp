class Solution {
public:
    int maxCoins(vector<int>& nums) {
        int n = nums.size();
        vector<vector<int>> dp(n, vector<int>(n, 0));

        for (int len = 0; len <= n; len++){
            for (int l = 0; l <= n-len; l++){
                // always same border for all k s
                int r = l + len - 1;
                int prev = 1;
                if (l != 0) {
                    prev = nums[l-1];
                }
                int nxt = 1;
                if (r != n-1) {
                    nxt = nums[r+1];
                }
                // consider each k in the subarray as the last popped balloon
                for (int k = l; k <= r; k++) {
                    int sub1 = 0;
                    if (k != l) {
                        sub1 =  dp[l][k-1];
                    }
                    int sub2 = 0;
                    if (k != r) {
                        sub2 = dp[k+1][r];
                    }
                    int cur = prev * nums[k] * nxt + sub1 + sub2;
                    if (dp[l][r] < cur) {
                        dp[l][r] = cur;
                    }
                }
            }
        }
        return dp[0][n-1];
    }
};
