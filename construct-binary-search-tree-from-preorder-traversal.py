class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        #base case
        if not preorder: return
        if len(preorder) == 1: return TreeNode(preorder[0])
        #create root from preorder[0] value
        root = TreeNode(preorder[0])
        #iterate through array to find left end and right start
        i = 1
        for j in range(1, len(preorder)):
            if preorder[j] < preorder[0]:
                i += 1
        #recursively call on left and right to build the tree
        root.left = self.bstFromPreorder(preorder[1:i])
        root.right = self.bstFromPreorder(preorder[i:])
        #return root of the created binary search tree
        return root