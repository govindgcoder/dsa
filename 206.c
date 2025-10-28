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
Node* reverseList(Node* head) {
   if(head==NULL) return NULL;
   Node *prev=NULL;
   Node *current=head;
   Node *next=current->next;
   while(current!=NULL){
      next=current->next;
      current->next=prev;
      prev=current;
      current=next;
   }
   return prev;

}

// ------------------------------------------------------------------
// TEST HARNESS
// ------------------------------------------------------------------
int main() {
    int arr1[] = {1, 2, 3, 4, 5};
    Node* head1 = createList(arr1, 5);
    printf("Original: ");
    printList(head1);
    
    head1 = reverseList(head1);
    
    printf("Reversed: ");
    printList(head1); // Expected: [ 5 -> 4 -> 3 -> 2 -> 1 -> NULL ]
    freeList(head1);

    printf("\n");

    int arr2[] = {1};
    Node* head2 = createList(arr2, 1);
    printf("Original: ");
    printList(head2);
    
    head2 = reverseList(head2);
    
    printf("Reversed: ");
    printList(head2); // Expected: [ 1 -> NULL ]
    freeList(head2);

    printf("\n");
    
    Node* head3 = NULL;
    printf("Original: ");
    printList(head3);
    
    head3 = reverseList(head3);
    
    printf("Reversed: ");
    printList(head3); // Expected: [ NULL ]
    freeList(head3);

    return 0;
}