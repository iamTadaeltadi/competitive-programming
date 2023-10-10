# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

        # Tree =TreeNod/e()

        def dfs(node1,node2):
            
            if not node1 and not node2:
                return True
            if not node1 or not node2:
                print("ads")
                return False
            print(node1.val,node2.val)
            if node1.val != node2.val:
                return False 
            elif (node1.left and node1.right ) and (not node2.right or not node2.left) or ((node2.left and node2.right ) and (not node1.right or not node1.left)):
                return False
            
            elif node1.left and node2.right and node1.left.val== node2.right.val:
                return dfs(node1.left,node2.right) and dfs(node1.right,node2.left)
            elif node2 and node2.left and node1 and node1.right and node2.left.val== node1.right.val:
                return dfs(node1.right,node2.left) and dfs(node1.left,node2.right)
            elif node2 and node2.left and node1 and node1.left and node2.left.val== node1.left.val:
                return dfs(node1.left,node2.left) and dfs(node1.right,node2.right)
            elif node2 and node2.right and node1 and node1.right and node2.right.val== node1.right.val:
                return dfs(node1.right,node2.right) and dfs(node1.left,node2.left)
            elif not node1.left and not node2.left and not node2.right and not node1.right:
                print("xxx")
                return True
            
            else:
                return False
            


        return dfs(root1,root2)