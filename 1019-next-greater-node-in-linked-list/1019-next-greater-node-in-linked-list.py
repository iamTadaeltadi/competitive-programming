# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def nextLargerNodes(self, head):
        """
        :type head: ListNode
        :rtype: List[int]
        """
        ans=[]
        while head:
            ans.append(head.val)
            head=head.next
        stack=[[ans[0],0]]
        res=[0]*len(ans)
        
        for i in range(1,len(ans)):
            while stack and stack[-1][0]<ans[i]:
                res[stack.pop()[1]]=ans[i]
            stack.append([ans[i],i])
        
        return res
                
                
                    
                
                
            
     