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
Node* mergeTwoLists(Node* list1, Node* list2) {
   Node *dummy=createNode(0);
   Node *current=dummy;
   Node *temp1=list1;
   Node *temp2=list2;
   while(temp1!=NULL&&temp2!=NULL){
      if(temp1->data<temp2->data){
         current->next=temp1;
         temp1=temp1->next;
         current=current->next;
      } else{
         current->next=temp2;
         temp2=temp2->next;
         current=current->next;
      }
   } 
   if(temp1!=NULL){
      current->next=temp1;
   }
   if(temp2!=NULL){
      current->next=temp2;
   }
   return dummy->next;
}

// ------------------------------------------------------------------
// TEST HARNESS
// ------------------------------------------------------------------
int main() {
    int arr1[] = {1, 2, 4};
    Node* list1 = createList(arr1, 3);
    
    int arr2[] = {1, 3, 4};
    Node* list2 = createList(arr2, 3);
    
    printf("List 1: ");
    printList(list1);
    printf("List 2: ");
    printList(list2);

    Node* merged = mergeTwoLists(list1, list2);
    
    printf("Merged: ");
    printList(merged); // Expected: [ 1 -> 1 -> 2 -> 3 -> 4 -> 4 -> NULL ]
    freeList(merged);

    printf("\n");

    Node* list3 = NULL;
    int arr4[] = {0};
    Node* list4 = createList(arr4, 1);

    printf("List 1: ");
    printList(list3);
    printf("List 2: ");
    printList(list4);

    Node* merged2 = mergeTwoLists(list3, list4);
    
    printf("Merged: ");
    printList(merged2); // Expected: [ 0 -> NULL ]
    freeList(merged2);
    
    return 0;
}