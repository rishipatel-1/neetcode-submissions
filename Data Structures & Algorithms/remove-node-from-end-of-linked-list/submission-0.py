class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        curr = head

        while curr:
            length += 1
            curr = curr.next

        target = length - n

        if target == 0:
            return head.next

        curr = head

        for _ in range(target-1):
            curr = curr.next

        curr.next = curr.next.next
        return head    

