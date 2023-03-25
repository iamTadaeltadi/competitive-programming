# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        res=node.next.val
        node.next.val=node.val
        node.next=node.next.next
        node.val=res
        
        # node.next.val=node.val
        # node.next=v.next.next
        # node=v
