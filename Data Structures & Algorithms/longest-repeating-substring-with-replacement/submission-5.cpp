class Solution {
public:
    int characterReplacement(string s, int k) {
        int l = 0;
        map<char, int> freq;
        int res = 0;
        for (int r = 0; r < s.size(); r++) {
            freq[s[r]] += 1;
            int m = 0;
            for (auto& [ch, f] : freq) {
                m = max(m, f);
            }
            while ( r -l + 1 - m > k ) {
                freq[s[l]] -= 1;
                l += 1;
            }
            res = max(res, r - l + 1);
        }
        return res;
    }
};
