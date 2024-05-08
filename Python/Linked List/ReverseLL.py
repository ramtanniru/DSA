class Solution:
    # recursion
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        if not head.next:
            return head
        temp = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return temp
    # iterative
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        prev,curr,nxt = head,head.next,head.next.next
        prev.next = None
        while nxt:
            curr.next = prev
            prev = curr
            curr = nxt
            nxt = nxt.next
        curr.next = prev
        return curr