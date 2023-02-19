# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        x=head.val
        y=ListNode(head.val,None)
       
        v=y
       
        while head:
            while head and head.val==x:
                head=head.next
            if head:
                x=head.val
                temp=head.next
                head.next=None
                y.next=head
                head=temp
                y=y.next
        return v
                
            
            
        