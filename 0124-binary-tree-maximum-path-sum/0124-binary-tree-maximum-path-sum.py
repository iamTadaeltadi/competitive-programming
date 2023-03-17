# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        arr=[]
        def maxPath(root):
            if not root:
                return 0
            leftMax=maxPath(root.left)
            rightMax=maxPath(root.right)
            currentNode=root.val
            res=max(leftMax+rightMax+currentNode,rightMax+currentNode,leftMax+currentNode,currentNode)
            arr.append(res)
            return max(rightMax+currentNode,leftMax+currentNode,currentNode)
        maxPath(root)
        return max(arr)
        
        