# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def __init__ (self):
        self.a = []

    def postorder(self,root):
            if root == None:
                return
            self.postorder(root.left)
            self.postorder(root.right)
            self.a.append(root.val)

        
        
    
    def postorderTraversal(self, root: TreeNode | None) -> list[int]:
        self.postorder(root)
        return self.a