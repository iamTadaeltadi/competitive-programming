class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        left = head
        right = self.getMid(head)
        temp = right.next
        right.next = None
        right = temp
        l = self.sortList(left)
        r = self.sortList(right)
        return self.merge(l, r)

    def merge(self, left, right):
        dummy = ListNode()
        merged = dummy
        while left and right:
            if left.val < right.val:
                merged.next = left
                left = left.next
            else:
                merged.next = right
                right = right.next
            merged = merged.next
        if left:
            merged.next = left
        if right:
            merged.next = right
        return dummy.next

    def getMid(self, head):
        slow, fast = head, head.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow
