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
        def build_bst(l, r):
            if l > r:
                return None
            
            mid = (l + r) // 2

            left_subtree = build_bst(l, mid - 1)

            nonlocal head
            root = TreeNode(val=head.val)
            root.left = left_subtree

            head = head.next  # Move to the next element in the linked list

            root.right = build_bst(mid + 1, r)

            return root

        # Count the number of elements in the linked list
        n = 0
        current = head
        while current:
            n += 1
            current = current.next

        return build_bst(0, n - 1)
