# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.arr=[]
        self.kSmallest(root,0)
        return self.arr[k-1]
    def kSmallest(self,root,level):
        if not root:
            return 
        
        self.kSmallest(root.left,level+1)
        self.arr.append(root.val)
        self.kSmallest(root.right,level+1)
        
    
    

        
        
        