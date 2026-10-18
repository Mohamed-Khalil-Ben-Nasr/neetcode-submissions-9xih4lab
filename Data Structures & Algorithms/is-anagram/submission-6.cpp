class Solution {
public:
    map<char, int> freqDict(string s){
        map<char,int> freq;
        for (char c : s) {
            freq[c]++;
        }
        return freq;
    }
    bool isAnagram(string s, string t) {
        if (s.size() != t.size()){
            return false;
        }
        map<char, int> f1 = freqDict(s);
        map<char, int> f2 = freqDict(t);
        for (char c : s) {
            if (f1[c] != f2[c]) {
                return false;
            }
        }
        return true;
    }
};
