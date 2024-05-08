class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr1,curr2 = list1,list2
        res = ListNode(0)
        head = res
        while curr1 and curr2:
            if curr1.val>curr2.val:
                head.next = ListNode(curr2.val)
                head = head.next
                curr2 = curr2.next
            else:
                head.next = ListNode(curr1.val)
                head = head.next
                curr1 = curr1.next
        while curr1:
            head.next = ListNode(curr1.val)
            head = head.next
            curr1 = curr1.next
        while curr2:
            head.next = ListNode(curr2.val)
            head = head.next
            curr2 = curr2.next
        return res.next