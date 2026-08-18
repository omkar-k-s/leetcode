class Solution(object):
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0)
        dummy.next = head

        slow = dummy
        fast = dummy

        # Create a gap of n + 1
        for i in range(n + 1):
            fast = fast.next

        # Move both pointers
        while fast:
            slow = slow.next
            fast = fast.next

        # Remove nth node
        slow.next = slow.next.next

        return dummy.next