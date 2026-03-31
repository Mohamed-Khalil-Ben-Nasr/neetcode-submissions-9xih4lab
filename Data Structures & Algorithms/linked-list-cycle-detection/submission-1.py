# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        s = set()

        cur = head
        while cur:
            if cur in s:
                return True
            s.add(cur)
            cur = cur.next
        
        return False
            