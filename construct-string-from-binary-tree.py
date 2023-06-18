# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        def map(root):
            if not root:
                return "()"

            if root and not root.left and not root.right:
                return f"({root.val})"
           
            l = map(root.left)
            r = map(root.right)
            if r=="()":
                return "("+str(root.val) + l +")"
            else:
                return "("+str(root.val) + l + r  +")"
               
        
        return map(root)[1:-1]