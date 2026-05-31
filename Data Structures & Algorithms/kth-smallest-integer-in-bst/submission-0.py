# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import heapq
from collections import deque
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        h = []
        # this is done in place and returns NONE
        heapq.heapify(h)
        # if two nodes have the same value, the heap will try to compare the second 
        # var in the list of type TREENODE, which cant be compared and will error
        # so only store value
        q = deque([root])
        while q:
            cur = q.popleft()
            heapq.heappush(h, cur.val)
            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)
        while (k-1) > 0:
            heapq.heappop(h)
            k -= 1
        return h[0]
        # the smallest element is always at index 0
