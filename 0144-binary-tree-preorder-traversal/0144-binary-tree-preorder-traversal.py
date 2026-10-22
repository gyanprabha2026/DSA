# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def __init__ (self):
        self.a = []

    def preorder(self,root):
            if root == None:
                return
            self.a.append(root.val)
            self.preorder(root.left)
            self.preorder(root.right)
   
    def preorderTraversal(self, root: TreeNode | None) -> list[int]:
        self.preorder(root)
        return self.a
        