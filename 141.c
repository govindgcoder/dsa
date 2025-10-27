#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h> // For bool, true, false

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

void freeList(Node* head) {
    Node* current = head;
    while (current != NULL) {
        Node* temp = current;
        current = current->next;
        free(temp);
    }
}
// ------------------------------------------------------------------

// YOUR FUNCTION GOES HERE
bool hasCycle(Node *head) {
    // Your implementation here
    return false; // Placeholder
}

// ------------------------------------------------------------------
// TEST HARNESS
// ------------------------------------------------------------------
int main() {
    Node* head1 = createTestList(5, 2); 
    printf("Test 1 (Cycle at pos 2): %s\n", hasCycle(head1) ? "true" : "false"); 

    Node* head2 = createTestList(5, -1); 
    printf("Test 2 (No cycle): %s\n", hasCycle(head2) ? "true" : "false"); 
    freeList(head2);

    Node* head3 = createTestList(0, -1);
    printf("Test 3 (Empty list): %s\n", hasCycle(head3) ? "true" : "false");
    freeList(head3);

    Node* head4 = createTestList(1, -1);
    printf("Test 4 (Single node): %s\n", hasCycle(head4) ? "true" : "false"); 
    freeList(head4);

    return 0;
}