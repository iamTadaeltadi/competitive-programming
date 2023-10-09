# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], target: int) -> int:
        dictt=defaultdict(int)
        dictt[0]=1
        prefix=0
        res=0
        def path(root):
            nonlocal prefix
            nonlocal res
            if not root:
                return 
            prefix+=root.val
            if prefix-target in dictt:
                res+=dictt[prefix-target]
                
            dictt[prefix]+=1
            
            path(root.left)
            path(root.right)
            
            dictt[prefix]-=1
            prefix-=root.val
            
        path(root)
        
        return res