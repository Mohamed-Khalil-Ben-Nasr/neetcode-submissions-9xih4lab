class Solution {
public:
    map<char, int> generateFreqMap(string s) {
        map<char, int> freq;
        for (char c : s) {
            freq[c]++;
        }
        return freq;
    }
    bool isAnagram(string s, string t) {
        if (s.size() != t.size()) {
            return false;
        }
        map<char, int> f1 = generateFreqMap(s);
        map<char, int> f2 = generateFreqMap(t);
        for (const auto& [key, value] : f1) {
            if (value != f2[key]) {
                return false;
            }
        }
        return true;
    }
};
