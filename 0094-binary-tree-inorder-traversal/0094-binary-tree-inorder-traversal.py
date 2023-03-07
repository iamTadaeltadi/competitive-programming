# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.res=[]
        self.rec(root)
        return self.res 
    
    
    def rec(self,node):
        if node:
            self.rec(node.left)
            self.res.append(node.val)
            self.rec(node.right)
        
            