class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False
        vals = set()
        while head:
            if head in vals:
                return True
            vals.add(head)
            head = head.next
        return False
