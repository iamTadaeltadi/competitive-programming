# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        x=head
        length=1
        while head:
            length+=1
            head=head.next
        n=(length-1)//2+1
        length=1
        while x:
            if length==n:
                return x
            x=x.next
            length+=1
        