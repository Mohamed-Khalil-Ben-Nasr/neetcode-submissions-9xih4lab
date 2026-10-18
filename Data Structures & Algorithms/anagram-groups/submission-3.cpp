class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        map<string, vector<string>> anagramBuckets;
        for (string s: strs) {
            string sortedS = s;
            sort(sortedS.begin(), sortedS.end());
            anagramBuckets[sortedS].push_back(s);
        }

        vector<vector<string>> res;
        for (auto& [key, bucket] : anagramBuckets) {
            res.push_back(bucket);
        }
        return res;
    }
};
