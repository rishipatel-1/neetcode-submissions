class Solution:
    def copyRandomList(self, head):

        copies = {None: None}

        curr = head

        while curr:

            copy = Node(curr.val)

            copies[curr] = copy

            curr = curr.next

        curr = head

        while curr:

            copy = copies[curr]

            copy.next = copies[curr.next]

            copy.random = copies[curr.random]

            curr = curr.next

        return copies[head]