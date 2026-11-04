class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        map<int, int> freq;
        for (auto& num : nums) {
            freq[num]++;
        }

        // min Heap is:
        // priority_queue< pair<int,int>, vector<pair<int,int>>, greater<pair<int,int>>>
        // priority_queue uses comparator to decide which elements have lower priority. 
        // In the case of minHeap, greater elements have lower priority
        priority_queue<pair<int, int>> maxHeap;
        for (auto& [num, f] : freq) {
            maxHeap.push({f, num});
        }

        vector<int> res;
        while (k > 0) {
            auto p = maxHeap.top();
            res.push_back(p.second);
            maxHeap.pop();
            k--;
        }

        return res;
    }
};
