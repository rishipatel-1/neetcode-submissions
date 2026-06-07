class Solution:
    def reorderList(self, head):
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second = slow.next
        slow.next = None

        prev = None

        while second:
            nxt = second.next
            second.next = prev

            prev = second
            second = nxt

        first = head 
        second = prev    

        while second:
            temp1 = first.next
            temp2 = second.next

            first.next = second
            second.next = temp1

            first = temp1
            second = temp2