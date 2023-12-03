# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        

        def insert(root,val):
            if not root:
                return 
            
            if root.val<val:
                root.right=insert(root.right,val)
            elif root.val>val:
                root.left=insert(root.left,val)
            else:

                if not root.left:
                    return root.right
                if not root.right:
                    return root.left
                cur=root.right

                while cur.left:
                    cur=cur.left

                root.val=cur.val
                root.right=insert(root.right,root.val)

            return root
        return insert(root,val)

                
                

            







            


        