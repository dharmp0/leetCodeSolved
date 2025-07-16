class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        curA = headA
        curB = headB

        while curA or curB:
            
            if curA == curB:
                return curA
            
            curA = curA.next if curA else headB
            curB = curB.next if curB else headA
        
        return None
