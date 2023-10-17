# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        dummy1 =l1
        dummy2 =l2

        prev = None

        while l1:
            nxt = l1.next
            l1.next = prev
            prev = l1
            l1 = nxt
        
        prev2 = None

        while l2:
            nxt = l2.next
            l2.next = prev2
            prev2 = l2
            l2 = nxt

        # return (prev,prev2)
        
        

       
        answer = tail = ListNode()
        remainder = 0

        while prev and prev2:

            
            sum_of_node = (prev.val +prev2.val +remainder)
            
            last_digit = sum_of_node%10
            remainder = sum_of_node//10
            tail.next = ListNode(last_digit)
            prev = prev.next
            prev2 = prev2.next
            tail = tail.next
        


        while prev:
            sum_of_node = (prev.val+remainder)
            last_digit = sum_of_node%10
            remainder = sum_of_node//10
            tail.next = ListNode(last_digit)
            tail = tail.next
            prev = prev.next
        

        while prev2:
            sum_of_node = (prev2.val+remainder)
            last_digit = sum_of_node%10
            remainder = sum_of_node//10
            tail.next = ListNode(last_digit)
            tail = tail.next
            prev2 = prev2.next
        
        if remainder >0:
            tail.next = ListNode(remainder)
            tail = tail.next

        answer = answer.next
        prev = None

        while answer:
            nxt =answer.next
            answer.next = prev
            prev = answer
            answer = nxt
        return prev