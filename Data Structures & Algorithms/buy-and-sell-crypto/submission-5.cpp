class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int res = 0;
        int l = 0;
        for (int r = 1; r < prices.size(); r++) {
            if (prices[r] < prices[l]) {
                l = r;
                continue;
            }
            res = max(res, prices[r] - prices[l]);
        }
        return res;
    }
};
