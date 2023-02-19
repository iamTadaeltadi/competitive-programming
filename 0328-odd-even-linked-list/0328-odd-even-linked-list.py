# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        odd=ListNode()
        even=ListNode()
        x=odd
        y=even
        count= 1
        while head:
            if count%2==1:
                odd.next=ListNode(head.val,None)
                odd=odd.next
            else:
                even.next=ListNode(head.val,None)
                even=even.next
            head=head.next
            count+=1
        x=x.next
        y=y.next
        t=x
        while x.next:
            x=x.next
        x.next=y
        return t
            
    
            
    