struct ListNode* createNode(int value) {
    struct ListNode* newNode = (struct ListNode*)malloc(sizeof(struct ListNode));
    newNode->val = value;
    newNode->next = NULL;
    return newNode;
}

struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2) {

     struct ListNode* dummy = createNode(0);
    struct ListNode* current = dummy;
    int carry = 0;
    
    while (l1 != NULL || l2 != NULL || carry != 0) {
        int sum = carry;
        
        if (l1 != NULL) {
            sum += l1->val;
            l1 = l1->next;
        }
        
        if (l2 != NULL) {
            sum += l2->val;
            l2 = l2->next;
        }
        
        carry = sum / 10;
        sum = sum % 10;
        
        current->next = createNode(sum);
        current = current->next;
    }
    
    return dummy->next;


}