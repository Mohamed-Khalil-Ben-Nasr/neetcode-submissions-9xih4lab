class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int l = 0;
        int res = 0;
        set<int> ss;
        for (int r = 0; r < s.size(); r++) {
            while (ss.contains(s[r])) {
                ss.erase(s[l]);
                l++;
            }
            ss.insert(s[r]);
            res = max(res, r - l + 1);
        }
        return res;
    }
};
