

class Solution(TreeNode):
    def minDepth(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0
        
        result = float("inf")
        
        def minimize(root, res):
            
            nonlocal result
            
            if not root:
                return 
            
            if not root.left and not root.right:     
                result = min(result, res)
                return
            
            minimize(root.left, res + 1)
            minimize(root.right, res + 1)
            
        minimize(root, 1)
        
        return result 