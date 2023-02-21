# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        orginal=ListNode()
        org=orginal
      
       
        prev=None
        length=0
        while head:
            if not orginal:
                orginal=ListNode(head.val,None)
            else:
                orginal.next=ListNode(head.val,None)
            temp=head.next
            head.next=prev
            prev=head
            head=temp
            length+=1
            orginal=orginal.next
        org=org.next
        count=0
        m=0
        while prev and count<(length)/2:
            twin_sum=prev.val+org.val
            m=max(twin_sum,m)
            prev=prev.next
            org=org.next
            count+=1
        return m
            
            
            
        
     
        
        