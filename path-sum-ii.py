# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans = []
        
        def dfs(root, path, path_sum):
            if not root:
                return 
            
            path.append(root.val)
            path_sum += root.val
            
            if not root.left and not root.right and path_sum == targetSum:
                ans.append(list(path))
            
            dfs(root.left, path, path_sum)
            dfs(root.right, path, path_sum)
            
            # Backtrack: remove the last element to backtrack the path
            path.pop()
        
        dfs(root, [], 0)
        return ans