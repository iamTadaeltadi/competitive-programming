# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        f=l1
        s=l2
        val=0
        remainder=0
        res=ListNode(None)
        ans=res
        tot=0
        while l1 and l2:
            tot=l1.val+l2.val+remainder
            remainder=tot//10
            val=tot%10
            res.next=ListNode(val)
            l1=l1.next
            l2=l2.next
            res=res.next
            
        while l1:
            tot=l1.val+remainder
            val=tot%10
            res.next=ListNode(val)
            l1=l1.next
            res=res.next
            remainder=tot//10
        while l2:
            tot=l2.val+remainder
            val=tot%10
            res.next=ListNode(val)
            l2=l2.next
            res=res.next
            remainder=tot//10
        if remainder >0:
            res.next=ListNode(remainder)
        res=res.next
        
        return ans.next
            
            

        