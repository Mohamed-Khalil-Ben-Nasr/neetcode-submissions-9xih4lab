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

        // distance between slow and fast is n+1
        while (n > 0 && fast) {
            fast = fast->next;
            n -= 1;
        }

        // now iterate until we reach end of linked list
        while (fast) {
            slow = slow->next;
            fast = fast->next;
        }

        // remove the nth node
        slow->next = slow->next->next;

        return dummy.next;
    }
};
