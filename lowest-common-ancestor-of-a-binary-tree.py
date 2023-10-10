# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ans = None

        def dfs(node):
            nonlocal ans
            if not node:
                return False

            left = dfs(node.left)
            right = dfs(node.right)
            current_node_matches = node.val == p.val or node.val == q.val

            if left + right + current_node_matches >= 2:
                ans = node

            return left or right or current_node_matches

        dfs(root)
        return ans