class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        map<int,int> freq;
        for (int num : nums) {
            freq[num]++;
        }
        priority_queue<pair<int,int>> maxHeap;
        for (auto& [num, f] : freq) {
            maxHeap.push({f, num});
        }
        vector<int> res;
        while (k>0) {
            auto pair = maxHeap.top();
            maxHeap.pop();
            res.push_back(pair.second);
            k--;
        }
        return res;
    }
};
