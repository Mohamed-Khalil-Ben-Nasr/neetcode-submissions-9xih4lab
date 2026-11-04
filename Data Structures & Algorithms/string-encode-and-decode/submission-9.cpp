class Solution {
public:

    string encode(vector<string>& strs) {
        string res;
        for (auto& s : strs) {
            res += to_string(s.size());
            res += "#";
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
            int length = stoi(s.substr(i, j - i));
            // skip the #
            i = j + 1;
            string curS = s.substr(i, length);
            res.push_back(curS);
            i += length;
        }
        return res;
    }
};
