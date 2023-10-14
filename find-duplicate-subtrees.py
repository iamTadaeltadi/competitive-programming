from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        # Dictionary to store the serialized subtrees and their occurrences
        subtree_count = {}

        # List to store the duplicate subtrees
        duplicates = []

        # Helper function to perform depth-first traversal and serialize subtrees
        def dfs(node):
            if not node:
                return "#"

            # Serialize the subtree using pre-order traversal
            serialized_tree = str(node.val) + "," + dfs(node.left) + "," + dfs(node.right)

            # Update the subtree count and check for duplicates
            subtree_count[serialized_tree] = subtree_count.get(serialized_tree, 0) + 1

            if subtree_count[serialized_tree] == 2:
                duplicates.append(node)

            return serialized_tree

        dfs(root)  # Start the serialization and duplicate detection
        return duplicates

# Example usage
# Create a binary tree
# root = TreeNode(1)
# root.left = TreeNode(2)
# root.right = TreeNode(3)
# root.left.left = TreeNode(4)
# root.right.left = TreeNode(2)
# root.right.right = TreeNode(4)
# root.right.left.left = TreeNode(4)

# solution = Solution()
# duplicates = solution.findDuplicateSubtrees(root)
# for duplicate in duplicates:
#     print(duplicate.val)