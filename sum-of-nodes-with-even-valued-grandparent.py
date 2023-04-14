# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        tot=0
        def recur(root,path):
            nonlocal tot
            if not root:
                return 
            if len(path)>=2:
                if path[-2]%2==0:
                    
                    
                    tot+=root.val


            recur(root.left,path+[root.val])
            recur(root.right,path+[root.val])
        recur(root,[])
        return tot