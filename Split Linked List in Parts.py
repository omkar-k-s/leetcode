class Solution(object):
    def splitListToParts(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: List[Optional[ListNode]]
        """

        n = 0
        curr = head
        while curr:
            n += 1
            curr = curr.next

        part_size = n // k
        extra = n % k

        result = []
        curr = head

        for i in range(k):
            if not curr:
                result.append(None)
                continue

            result.append(curr)

            size = part_size
            if i < extra:
                size += 1

            for j in range(size - 1):
                curr = curr.next
       
            next_part = curr.next
            curr.next = None
            curr = next_part
        return result