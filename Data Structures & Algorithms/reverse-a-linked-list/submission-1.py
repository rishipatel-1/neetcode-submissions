class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        prev = None
        current = head 

        while current:
            nxt = current.next
            current.next = prev

            prev = current
            current = nxt

        return prev    


        