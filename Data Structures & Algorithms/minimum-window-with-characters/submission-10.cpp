class Solution {
public:
    string minWindow(string s, string t) {
        if (s.size() < t.size()) {
            return "";
        }

        unordered_map<char, int> dt;
        for (char c : t) {
            dt[c] += 1;
        }

        size_t need = dt.size();
        size_t have = 0;
        unordered_map<char, int> ds;
        size_t bestLength = SIZE_MAX;
        size_t bestStart = 0;
        size_t l = 0;
        for (size_t r = 0; r < s.size(); r++) {
            if (dt.find(s[r]) != dt.end()) {
                ds[s[r]] += 1;
                if (ds[s[r]] == dt[s[r]]) {
                    have += 1;
                }
            }

            while (need == have) {
                if ( (r - l + 1) < bestLength) {
                    bestLength = r - l + 1;
                    bestStart = l;
                }
                if (dt.find(s[l]) != dt.end()) {
                    ds[s[l]] -= 1;
                    if (ds[s[l]] < dt[s[l]]) {
                        have -= 1;
                    }
                }
                l += 1;
            }
        }
        return (bestLength == SIZE_MAX) ? "" : s.substr(bestStart, bestLength);
    }
};
