class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head or not head.next:
            return None


        fast = head.next.next
        slow = head
        
        while fast and fast.next:
            
            fast = fast.next.next
            slow = slow.next
        
        slow.next = slow.next.next

        return head
