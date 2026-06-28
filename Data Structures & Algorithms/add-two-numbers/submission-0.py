# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        i = 0
        num1 = 0
        num2 = 0
        while l1 or l2:
            if l1:
                num1 += (10 ** i) *l1.val
                l1 = l1.next
            if l2:
                num2 += (10 ** i )* l2.val
                l2 = l2.next
            i += 1
        print("num1 ", num1)
        print("num2 ", num2)
        s = num1 + num2
        print(s)
        st = str(s)
        print("st ", st)
        res = ListNode()
        cur = res
        for i in range(len(st)-1,-1,-1):
            new = ListNode()
            new.val = int(st[i])
            print("new.val ", new.val)
            cur.next = new
            cur = cur.next
        return res.next
        

