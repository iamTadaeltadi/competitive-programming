# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        
        return self.kSmallest(root,0)[k-1]
    def kSmallest(self,root,level):
        if  not root :
            return None
        
        l=self.kSmallest(root.left,level+1)
        
        r=self.kSmallest(root.right,level+1)

        if l and r :
            return l + [root.val] + r
        if l:
            return l + [root.val]
        if r:
            return [root.val]+r
        return [root.val]