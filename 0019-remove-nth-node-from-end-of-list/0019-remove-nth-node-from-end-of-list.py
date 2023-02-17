# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        prev=None
        x=head
        while x :
            nxt=x.next
            x.next=prev
            prev=x
            x=nxt
        if n==1:
            prev=prev.next
            v=None
            while prev:
                nxt=prev.next
                prev.next=v
                v=prev
                prev=nxt
            
            return v
        
        t=prev
        for i in range(n-2):
            prev=prev.next
     
        prev.next=prev.next.next
        new=None 
        y=t
        while y :
            nxt=y.next
            y.next=new
            new=y
            y=nxt
        return new
        
    
    
            
            
    
        
            
            
        
     
        
        