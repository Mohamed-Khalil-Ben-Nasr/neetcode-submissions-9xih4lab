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
    void reorderList(ListNode* head) {
        ListNode* slow = head;
        ListNode* fast = head;
        while (fast && fast->next) {
            slow = slow->next;
            fast = fast->next->next;
        }

        ListNode* prev = nullptr;
        ListNode* cur = slow->next;
        slow->next = nullptr;

        while (cur) {
            ListNode* tmp = cur->next;
            cur->next = prev;
            prev = cur;
            cur = tmp;
        }

        ListNode* head2 = prev;
        ListNode dummy;
        cur = &dummy; 
        while(head && head2) {
            cur->next = head;
            head = head->next;
            cur->next->next = head2;
            head2 = head2->next;
            cur = cur->next->next;
        }
        if (head) {
            cur->next = head;
        }
        if (head2) {
            cur->next = head2;
        }
    }
};
