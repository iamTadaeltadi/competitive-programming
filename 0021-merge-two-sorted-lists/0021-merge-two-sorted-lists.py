# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        return self.merge(list1,list2)
        
    def merge(self,l1,l2):
        if not l1:
            return l2
        if not l2:
            return l1
        if l1.val <l2.val:
            l1.next=self.merge(l1.next,l2)
            return l1
        else:
            l2.next=self.merge(l1,l2.next)
            return l2
        
            
            
     
       
        