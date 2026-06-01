# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        m = float("-inf")
    
        # since we need a global var to track the max path sum when we recurse 
        # we need a helper function for the dfs
        def dfs(root):
            nonlocal m # tells Python "m is from the enclosing function"
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            # ignore any negative branch
            cur_path_sum = max(left,0) + max(right,0) + root.val
            # update global max
            m = max(m, cur_path_sum)
            # pass max branch to parent
            return root.val + max(left,right,0)
        
        dfs(root)
        return m
