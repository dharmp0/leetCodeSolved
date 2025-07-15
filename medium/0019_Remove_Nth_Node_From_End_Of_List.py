class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        if not head or not head.next:
            return None
        
        dummy = ListNode(0, head)
        fast = dummy
        slow = dummy


        for _ in range(n+1):
            fast = fast.next
        
        while fast:

            fast = fast.next
            slow = slow.next
        
        slow.next = slow.next.next
        
        return dummy.next
