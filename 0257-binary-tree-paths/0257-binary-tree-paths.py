class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.res=[]
class Solution(TreeNode):
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def allpath(root,path):
            path+=str(root.val)
            if not root.left and not root.right :
                self.res.append(path)
            if root.left:
                allpath(root.left,path+'->')
            if root.right:
                allpath(root.right,path+"->")
        allpath(root,"")
        return self.res
        