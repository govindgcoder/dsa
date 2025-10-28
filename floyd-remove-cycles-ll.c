#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h> 

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

Node* createTestList(int n, int pos) {
    if (n == 0) return NULL;
    Node* head = createNode(1);
    Node* current = head;
    Node* cycleNode = NULL;

    if (pos == 0) cycleNode = head;

    for (int i = 2; i <= n; i++) {
        current->next = createNode(i);
        current = current->next;
        if (i == pos + 1) {
            cycleNode = current;
        }
    }
    
    if (cycleNode != NULL) {
        current->next = cycleNode;
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
void detectAndRemoveCycle(Node* head) {
   Node* slow=head;
   Node* fast=head;

   while(fast != NULL && fast->next != NULL){
      slow=slow->next;
      fast=fast->next->next;
      if(slow==fast) break;
   }

   if(fast->next==NULL){
      return;
   }

   slow=head;
   while(fast!=slow){
      slow=slow->next;
      fast=fast->next;
   }
   Node *current=fast;
   while(current->next!=fast){
      current=current->next;
   }
   current->next=NULL;
   return;
   
}

// ------------------------------------------------------------------
// TEST HARNESS
// ------------------------------------------------------------------
int main() {
    // Test 1: A list with a cycle
    // 1 -> 2 -> 3 -> 4 -> 5
    //           ^         |
    //           |_________|
    Node* head1 = createTestList(5, 2); // Cycle at pos 2 (node 3)
    printf("Test 1 (Cycle at pos 2)\n");
    
    detectAndRemoveCycle(head1);
    
    printf("After removal: ");
    printList(head1); // Expected: [ 1 -> 2 -> 3 -> 4 -> 5 -> NULL ]
    freeList(head1);

    // Test 2: A list with no cycle
    Node* head2 = createTestList(5, -1); // No cycle
    printf("\nTest 2 (No cycle)\n");
    
    detectAndRemoveCycle(head2);
    
    printf("After removal: ");
    printList(head2); // Expected: [ 1 -> 2 -> 3 -> 4 -> 5 -> NULL ]
    freeList(head2);

    // Test 3: Cycle at head
    Node* head3 = createTestList(4, 0); // Cycle at pos 0 (node 1)
    printf("\nTest 3 (Cycle at head)\n");
    
    detectAndRemoveCycle(head3);
    
    printf("After removal: ");
    printList(head3); // Expected: [ 1 -> 2 -> 3 -> 4 -> NULL ]
    freeList(head3);
    
    return 0;
}