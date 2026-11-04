class Solution {
public:
    bool isValid(string s) {
        unordered_map<char, char> closeToOpen;
        closeToOpen[')'] = '(';
        closeToOpen['}'] = '{';
        closeToOpen[']'] = '[';
        stack<char> st;
        for (char c : s) {
            if (closeToOpen.contains(c)) {
                if (st.empty() || st.top() != closeToOpen[c]) {
                    return false;
                }
                st.pop();
            } else {
                st.push(c);
            }
        }
        return st.empty();
    }
};
