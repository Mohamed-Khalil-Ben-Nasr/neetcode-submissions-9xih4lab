class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        set<int> s;
        for (auto& num : nums) {
            s.insert(num);
        }
        int res = 0;
        for (auto& num: nums) {
            if (s.contains(num-1)) {
                continue;
            }
            int cur = num;
            int curL = 0;

            while (s.contains(cur)){
                cur++;
                curL++;
            }
            res = max(curL, res);
        }
        return res;
    }
};
