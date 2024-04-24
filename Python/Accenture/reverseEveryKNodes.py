# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr = head
        prev = None
        cnt = 0
        while curr and cnt<k:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            cnt += 1
        if curr:
            head.next = self.reverseKGroup(curr,k)
        return prev