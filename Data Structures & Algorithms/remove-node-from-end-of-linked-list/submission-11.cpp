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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode dummy;
        dummy.next = head;
        ListNode* slow = &dummy;
        ListNode* fast = head;

        // invariant: fast is ahead of slow by n nodes
        for (int i = 0; i < n; i++) {
            fast = fast->next;
        }
        // slow lands at the node right before the node that needs to be deleted
        while (fast != nullptr) {
            fast = fast->next;
            slow = slow->next;
        }

        slow->next = slow->next->next;
        return dummy.next;
    }
};
