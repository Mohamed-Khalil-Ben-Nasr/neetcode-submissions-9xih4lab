/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:
    bool hasCycle(ListNode* head) {
        set<ListNode*> s;
        ListNode* cur = head;
        while (cur) {
            if (s.contains(cur)) {
                return true;
            }
            s.insert(cur);
            cur = cur->next;
        }
        return false;
    }
};
