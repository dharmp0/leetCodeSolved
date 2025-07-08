class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        if head is None or head.next is None:
            return head
        
        prev = None
        curr = head
        count = 1

        while curr:
        
            if count == left:
               
                tail = prev
                front = curr

                while curr and count <= right:
                   
                    nextn = curr.next
                    curr.next = prev
                    prev = curr
                    curr = nextn
                    count += 1
                
                front.next = curr
                
                if tail:
                    tail.next = prev
                    return head
                else:
                    return prev
            
            prev = curr
            curr = curr.next
            count += 1
