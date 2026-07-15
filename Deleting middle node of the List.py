class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteMiddle(self, head):

        if head.next is None:
            return None

        slow = head
        fast = head
        prev = None

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        prev.next = slow.next
        return head

head = ListNode(1)
head.next = ListNode(3)
head.next.next = ListNode(4)
head.next.next.next = ListNode(7)
head.next.next.next.next = ListNode(1)

ans = Solution().deleteMiddle(head)

while ans:
    print(ans.val, end=" ")
    ans = ans.next