/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* deleteMiddle(struct ListNode* head) {
    if(head == NULL || head->next == NULL){
        return NULL;
    }

    struct ListNode *fast = head->next->next;
    struct ListNode *slow = head;

    while(fast != NULL && fast->next != NULL){
        fast = fast->next->next;
        slow = slow->next;
    }

    slow->next = slow->next->next;

    return head;
}
