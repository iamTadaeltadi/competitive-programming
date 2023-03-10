# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        rightView={}
        def rview(root,level):
            if not root:
                return 
            rightView[level]=root.val
            rview(root.left,level+1)
            rview(root.right,level+1)
        rview(root,0)
        return rightView.values()
            
        