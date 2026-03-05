# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow, fast = head, head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        prev = None
        curr = slow

        while curr:
            nextn = curr.next
            curr.next = prev
            prev = curr
            curr = nextn
        
        first = head
        second = prev

        while second.next:        
            
            tmp1 = first.next
            tmp2 = second.next

            first.next = second   
            second.next = tmp1   
            
            first = tmp1          
            second = tmp2   
