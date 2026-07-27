class Solution:
    def reverseBetween(self, head, left, right):

        dummy = ListNode(0)
        dummy.next = head

        prev = dummy

        # Move to node before 'left'
        for _ in range(left - 1):
            prev = prev.next

        tail = prev.next
        curr = tail
        previous = None

        # Reverse right-left+1 nodes
        for _ in range(right - left + 1):

            nxt = curr.next
            curr.next = previous
            previous = curr
            curr = nxt

        # Reconnect
        prev.next = previous
        tail.next = curr

        return dummy.next