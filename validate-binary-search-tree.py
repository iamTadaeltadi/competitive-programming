class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def rec(root, min_val, max_val):
            if root is None:
                return True

            if root.val <= min_val or root.val >= max_val:
                return False

            return (
                rec(root.left, min_val, root.val) and
                rec(root.right, root.val, max_val)
            )

        return rec(root, float('-inf'), float('inf'))