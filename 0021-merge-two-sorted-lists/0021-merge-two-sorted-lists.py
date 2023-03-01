# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        self.dummy = ListNode()
        self.answer = self.dummy
        def rec(l1, l2):
            if not l1 or not l2:
                self.dummy.next = l1
                if l2:
                    self.dummy.next = l2
                return 
            
            if l1.val < l2.val:
                self.dummy.next = l1
                self.dummy = self.dummy.next
                rec(l1.next, l2)
            else:
                self.dummy.next = l2
                self.dummy = self.dummy.next
                rec(l1, l2.next)
                
                
        rec(list1, list2)  
        return self.answer.next
            
     
       
        