# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(root, subRoot):
            # is same tree problem
            if not root and not subRoot:
                return True
            
            if not root or not subRoot:
                return False
            
            return (isSameTree(root.left, subRoot.left) and 
                isSameTree(root.right, subRoot.right) and
                root.val == subRoot.val)

        # null can be sub tree of root
        if root and not subRoot:
            return True
        
        # subRoot cant be sub tree of null
        if not root and subRoot:
            return False
        
        if isSameTree(root, subRoot):
            return True

        left = self.isSubtree(root.left, subRoot)
        right = self.isSubtree(root.right, subRoot)

        return left or right
            
        
        