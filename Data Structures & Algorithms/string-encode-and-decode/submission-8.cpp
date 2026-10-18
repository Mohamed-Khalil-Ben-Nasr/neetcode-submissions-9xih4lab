class Solution {
public:

    string encode(vector<string>& strs) {
        string res = "";
        for (auto& s : strs) {
            res += to_string(s.size());
            res.push_back('#');
            res += s;
        }
        return res;
    }

    vector<string> decode(string s) {
        vector<string> res;
        int i = 0;
        while (i < s.size()) {
            int j = i;
            while (j < s.size() && s[j] != '#'){
                j++;
            }
            int length = stoi(s.substr(i, j-i));
            i = j;
            // skip #
            i++;
            // get the actual string
            string cur = s.substr(i, length);
            res.push_back(cur);
            i += length;
        }
        return res;
    }
};
