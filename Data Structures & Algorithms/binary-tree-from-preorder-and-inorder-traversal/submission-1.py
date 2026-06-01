# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Preorder tells you what the root is. 
        # Inorder tells you how to split the remaining elements into left and right subtrees. 
        # They're complementary — each one fills in exactly what the other is missing.
        
        # very important insight
        # Preorder gives you the root from the front, postorder gives you the root from the back 
        # — but neither tells you where the left subtree ends and the right begins. 
        # Without inorder, you have no way to split.

        # base case for null nodes
        if not preorder or not inorder:
            return None
        
        root = TreeNode(val = preorder[0])
        root_index = inorder.index(root.val)
        # in inorder array, everything to left of root belongs to left subtree
        # and to the right belongs to right subtree
        # length of the left subtree = root_index
        root.left =  self.buildTree(preorder[1:root_index+1], inorder[:root_index])
        root.right = self.buildTree(preorder[root_index+1:], inorder[root_index+1:])
        return root