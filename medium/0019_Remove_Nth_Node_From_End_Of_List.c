struct ListNode* removeNthFromEnd(struct ListNode* head, int n) {
    if(head == NULL || head->next == NULL){
        return NULL;
    }

    struct ListNode* dummy = malloc(sizeof(struct ListNode));
    dummy->next = head;
    struct ListNode *fast = dummy;
    struct ListNode *slow = dummy;

    while(n>=0){
        fast = fast->next;
        n -= 1;
    }

    while(fast != NULL){
        fast = fast->next;
        slow = slow ->next;
    }

    slow->next = slow->next->next;

    return dummy->next;

}
