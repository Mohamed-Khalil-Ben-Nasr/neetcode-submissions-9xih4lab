class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        set<int> s;
        for (int num : nums){
            if (s.count(num)>0){
                return true;
            }
            s.insert(num);
        }
        return false;
    }
};