# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        d=defaultdict(list)
        ans=[]
        def inorder(root,level):
            
            if not root:
                return None
            d[level].append(root.val)
            left=inorder(root.left,level+1)
            right=inorder(root.right,level+1)
        inorder(root,0)
        for i in d:
            ans.append(d[i])
        return ans
