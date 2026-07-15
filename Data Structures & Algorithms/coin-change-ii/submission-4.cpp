class Solution {
private:
    vector<vector<int>> dp;
    int dfs(int i, int cur, int amount, vector<int>& coins) {
        if (i >= coins.size() or cur > amount) {
            return 0;
        }
        if (cur == amount) {
            return 1;
        }
        if (dp[i][cur] != -1) {
            return dp[i][cur];
        }
        // include path
        int include = dfs(i, cur+coins[i], amount, coins);
        // exclude 
        int exclude = dfs(i+1, cur, amount, coins);
        
        dp[i][cur] = include + exclude;
        return dp[i][cur];
    }
public:
    int change(int amount, vector<int>& coins) {
        dp.resize(coins.size());
        for (int i = 0; i < dp.size(); i++){
            dp[i].resize(amount, -1);
        }
       return dfs(0, 0, amount, coins);
    }
};
