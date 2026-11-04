class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        set<int> seen;
        for (auto& num : nums) {
            seen.insert(num);
        }

        int res = 0;
        for (auto& num : nums) {
            if (seen.contains(num-1)) {
                continue;
            }
            int cur = num;
            int l = 1;
            while (seen.contains(cur+1)){
                cur += 1;
                l += 1;
            }
            res = max(l, res);
        }

        return res;
    }
};
