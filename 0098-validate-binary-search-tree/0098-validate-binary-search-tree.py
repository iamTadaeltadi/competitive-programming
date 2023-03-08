# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.helper(-sys.maxsize, sys.maxsize, root)
    
    def helper(self, lower, upper, node):
        if not node:
            return True
        if node.val < lower or node.val > upper:
            return False
        return self.helper(lower, node.val - 1, node.left) and self.helper(node.val + 1, upper, node.right)
            