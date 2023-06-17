# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        def solve(curNode):
            if not curNode:
                return ''

            subString = str(curNode.val)
            #If curNode has no children
            if not curNode.left and not curNode.right:
                return subString

            subString += '(' + solve(curNode.left) + ')'
            if curNode.right:
                subString += '(' + solve(curNode.right) + ')'

            return subString

        return solve(root)