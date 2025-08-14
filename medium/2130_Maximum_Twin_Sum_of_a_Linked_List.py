class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        if not head or not head.next:
            return head
        
        slow = head
        fast = head.next.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        half = slow.next
        slow.next = None

        prev = None
        while half:
            nextn = half.next
            half.next = prev
            prev = half
            half = nextn
        
        msum = 0

        while head:
            csum = prev.val + head.val
            if csum>msum:
                msum = csum
            head = head.next
            prev = prev.next
        
        return msum
