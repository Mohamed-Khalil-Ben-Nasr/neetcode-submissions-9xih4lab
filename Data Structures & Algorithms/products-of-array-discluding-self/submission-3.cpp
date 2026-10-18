class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> pref(nums.size());
        pref[0] = 1;
        for (int i = 1; i < nums.size(); i++ ) {
            pref[i] = pref[i-1] * nums[i-1];
        }
        
        vector<int> suff(nums.size());
        suff[nums.size()-1] = 1;
        for (int i = nums.size()-2; i >= 0; i--) {
            suff[i] = suff[i+1] * nums[i+1];
        }

        vector<int> res(nums.size());
        for (int i = 0; i < nums.size(); i++) {
            res[i] = pref[i] * suff[i];
        }

        return res;
    }
};
