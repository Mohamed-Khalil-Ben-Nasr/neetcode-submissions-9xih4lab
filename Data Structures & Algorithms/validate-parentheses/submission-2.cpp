class Solution {
public:
    bool isValid(string s) {
        stack<char> st;
        map<char,char> d;
        d[']'] = '[';
        d[')'] = '(';
        d['}'] = '{';
        for (char c : s) {
            if (d.contains(c)) {
                if (st.size() == 0) {
                    return false;
                }
                char op = st.top();
                if (op != d[c]) {
                    return false;
                }
                st.pop();
            } else {
                st.push(c);
            }
        }
        return st.size() == 0;
    }
};
