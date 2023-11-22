# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:


        to_list = []

        while head:
            to_list.append(head.val)
            head = head.next
        
        

        n = len(to_list)

        def inbound(point) :
            return 0< point < n 

        
        
        def dfs(l,r):
            mid = l + (r-l)//2
            

            if r<l :
                return None
            root = TreeNode(to_list[mid])

            
            root.left = dfs(l,mid-1)
            root.right = dfs(mid+1,r)
            

            return root

        return dfs(0,n-1)
