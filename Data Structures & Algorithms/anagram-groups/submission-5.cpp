class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> anagramBuckets;
        for (auto& s : strs) {
            string c = s;
            sort(c.begin(), c.end());
            anagramBuckets[c].push_back(s);
        }
        vector<vector<string>> res;
        for (auto& [anagram, values] : anagramBuckets) {
            res.push_back(values);
        }
        return res;
    }
};
