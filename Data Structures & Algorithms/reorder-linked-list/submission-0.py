class Solution:
    def reorderList(self, head):

        # STEP 1: Find middle
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # STEP 2: Split list into two halves
        second = slow.next
        slow.next = None

        # STEP 3: Reverse second half
        prev = None

        while second:

            nxt = second.next
            second.next = prev

            prev = second
            second = nxt

        # STEP 4: Merge two halves
        first = head
        second = prev

        while second:

            tmp1 = first.next
            tmp2 = second.next

            first.next = second
            second.next = tmp1

            first = tmp1
            second = tmp2