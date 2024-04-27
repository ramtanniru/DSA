class Solution:
    def mergeSort(self, head):
        if not head or not head.next:
            return head
        mid = self.getMiddle(head)
        midNext = mid.next
        mid.next = None
        left = self.mergeSort(head)
        right = self.mergeSort(midNext)
        return self.merge(left,right)
        
    def merge(self,left,right):
        res = None
        if not left:
            return right
        if not right:
            return left
        if left.data<=right.data:
            res = left
            res.next = self.merge(left.next,right)
        else:
            res = right
            res.next = self.merge(left,right.next)
        return res
        
    def getMiddle(self,head):
        slow,fast = head,head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow