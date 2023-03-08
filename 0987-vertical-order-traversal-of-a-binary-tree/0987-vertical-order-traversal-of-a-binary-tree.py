# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        dictt=defaultdict(list)
        dictt=self.cols(dictt,0,0,root)
        dictt = sorted(dictt.items())
        dictt = [i[1] for i in dictt]
        res=[]
        for val in dictt:
            val.sort()
            col=[]
            for i in val:
                col.append(i[1])
            res.append(col)
        return res
    def cols(self, col_dict, row, col, root):
        
        if root is None:
            return col_dict
        col_dict[col].append([row,root.val])
        
        col_dict = self.cols(col_dict,row+1,col-1,root.left)
        col_dict = self.cols(col_dict,row+1,col+1,root.right)
        return col_dict