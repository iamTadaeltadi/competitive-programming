# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:

        
        

        def preorderTraverse(root):

            if not root:
                return 
            
            root.left = preorderTraverse(root.left)
            root.right = preorderTraverse(root.right)

            if root.val  in to_delete:
                if root.left:
                    disjoint.append(root.left)
                if root.right:
                    disjoint.append(root.right)
                return None 
            return root


        disjoint = []

        if root.val not in to_delete:
            disjoint.append(root)
            

        
    
        preorderTraverse(root)
        return disjoint

            

            
           