#include <stdio.h>
#include <stdlib.h>

// --- Helper Code ---
typedef struct Node {
    int data;
    struct Node* next;
} Node;

Node* createNode(int data) {
    Node* newNode = (Node*)malloc(sizeof(Node));
    if (newNode == NULL) exit(1);
    newNode->data = data;
    newNode->next = NULL;
    return newNode;
}

Node* createList(int* arr, int n) {
    if (n == 0) return NULL;
    Node* head = createNode(arr[0]);
    Node* current = head;
    for (int i = 1; i < n; i++) {
        current->next = createNode(arr[i]);
        current = current->next;
    }
    return head;
}

void printList(Node* head) {
    printf("List: [ ");
    Node* current = head;
    while (current != NULL) {
        printf("%d -> ", current->data);
        current = current->next;
    }
    printf("NULL ]\n");
}

void freeList(Node* head) {
    while (head != NULL) {
        Node* temp = head;
        head = head->next;
        free(temp);
    }
}
// ------------------------------------------------------------------

// YOUR FUNCTION GOES HERE
Node* removeNthFromEnd(Node* head, int n) {
    Node *dummy=createNode(0);
    dummy->next=head;
    Node *slow = dummy;
    Node *fast = dummy;
    
    for(int i=0;i<n;i++){
      fast=fast->next;
    }

    while(fast->next!=NULL){
      slow=slow->next;
      fast=fast->next;
    }

    Node *temp=slow->next;
    slow->next=slow->next->next;
    free(temp);

    Node *newHead = dummy->next;
    return newHead;

}

// ------------------------------------------------------------------
// TEST HARNESS
// ------------------------------------------------------------------
int main() {
    int arr1[] = {1, 2, 3, 4, 5};
    Node* head1 = createList(arr1, 5);
    printf("Original: ");
    printList(head1);
    
    head1 = removeNthFromEnd(head1, 2);
    
    printf("Removed 2nd from end: ");
    printList(head1); // Expected: [ 1 -> 2 -> 3 -> 5 -> NULL ]
    freeList(head1);

    printf("\n");

    int arr2[] = {1};
    Node* head2 = createList(arr2, 1);
    printf("Original: ");
    printList(head2);
    
    head2 = removeNthFromEnd(head2, 1);
    
    printf("Removed 1st from end: ");
    printList(head2); // Expected: [ NULL ]
    freeList(head2);

    printf("\n");
    
    int arr3[] = {1, 2};
    Node* head3 = createList(arr3, 2);
    printf("Original: ");
    printList(head3);
    
    head3 = removeNthFromEnd(head3, 2);
    
    printf("Removed 2nd from end (head): ");
    printList(head3); // Expected: [ 2 -> NULL ]
    freeList(head3);

    return 0;
}