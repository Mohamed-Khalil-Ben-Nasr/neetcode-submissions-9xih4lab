class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int l = 0;
        int res = 0;
        unordered_set<char> seen;
        for (int r = 0; r < s.size(); r++) {
            // shrink the window until all chars in window are distinct
            while (seen.contains(s[r])) {
                seen.erase(s[l]);
                l += 1;
            }
            seen.insert(s[r]);
            res = max(res, r - l + 1);
        }
        return res;
    }
};
