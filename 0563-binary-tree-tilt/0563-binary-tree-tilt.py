class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        total=[]
        def tlit(root):
            if not root:
                return 0
            leftChild=tlit(root.left)
            rightChild=tlit(root.right)
            total.append(abs(rightChild-leftChild))
            return rightChild+leftChild+root.val
        tlit(root)
        print(total)
     
        return sum(total)
            
            