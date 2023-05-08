class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Convert the list of linked lists into a flat list of values
        res=ListNode()
        dummy=res
        heap=[]
        for arr_idx in range(len(lists)):

        
            if lists[arr_idx]:
                heapq.heappush(heap,[lists[arr_idx].val,arr_idx])
                lists[arr_idx]=lists[arr_idx].next
        

        while heap:
            val,arr_idx=heapq.heappop(heap)
            dummy.next=ListNode(val)
            dummy=dummy.next
            if lists[arr_idx]:
                
                heapq.heappush(heap,[lists[arr_idx].val,arr_idx])
                lists[arr_idx]=lists[arr_idx].next
        return res.next