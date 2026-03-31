# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        q = deque()
        q.append(root)
        level = 0
        while q:
            for i in range(len(q)):
                cur = q.popleft()
                if cur.right:
                    q.append(cur.right)
                if cur.left:
                    q.append(cur.left)
            level += 1
        
        return level