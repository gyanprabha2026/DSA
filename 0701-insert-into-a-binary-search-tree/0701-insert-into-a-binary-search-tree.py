# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode | None, val: int) -> TreeNode | None:
        newnode = TreeNode(val)
        
        if root is None:
            return newnode
        
        curr = root
        while curr != None:
            if val < curr.val:
                if curr.left == None:
                    curr.left = newnode
                    break  
                curr = curr.left
            elif val > curr.val:
                if curr.right == None:
                    curr.right = newnode
                    break  
                curr = curr.right
                
        return root