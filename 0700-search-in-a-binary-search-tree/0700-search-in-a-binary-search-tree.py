
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.res=None
class Solution(TreeNode):
    def searchBST(self, root: Optional[TreeNode], val: int) ->Optional[TreeNode]:
        
        if root :
            if  root.val==val:
                self.res=root
                return self.res
            self.searchBST(root.left,val)
            self.searchBST(root.right,val)
        return self.res
        
    
        
    