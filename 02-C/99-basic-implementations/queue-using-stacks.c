#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

#define MAX_SIZE 100 

typedef struct {
    int items[MAX_SIZE];
    int top;             
} Stack;

Stack* createStack() {
    Stack* s = (Stack*)malloc(sizeof(Stack));
    if (s == NULL) exit(1);
    s->top = -1; 
    return s;
}

bool isEmpty(Stack* s) {
    return s->top == -1;
}

bool isFull(Stack* s) {
    return s->top == MAX_SIZE - 1;
}

void push(Stack* s, int data) {
    if (isFull(s)) {
        return; 
    }
    s->top++;
    s->items[s->top] = data;
}

int pop(Stack* s) {
    if (isEmpty(s)) {
        return -1; 
    }
    int item = s->items[s->top];
    s->top--;
    return item;
}

int peek(Stack* s) {
    if (isEmpty(s)) {
        return -1; 
    }
    return s->items[s->top];
}

void freeStack(Stack* s) {
    free(s);
}

typedef struct {
    Stack* s1; 
    Stack* s2; 
} MyQueue;

MyQueue* myQueueCreate() {
    MyQueue* q = (MyQueue*)malloc(sizeof(MyQueue));
    if (q == NULL) exit(1);
    q->s1 = createStack();
    q->s2 = createStack();
    return q;
}
bool myQueueIsEmpty(MyQueue* q) {
    if(isEmpty(q->s1)&&isEmpty(q->s2)) return true;
    return false; 
}
void myQueueEnqueue(MyQueue* q, int data) {
   if(isFull(q->s1)||isFull(q->s2)) return; 
   int temp;
   push(q->s1, data);
}

int myQueueDequeue(MyQueue* q) {
    if(myQueueIsEmpty(q)==true) return -1;
    int temp;
      if(isEmpty(q->s2)){while(!isEmpty(q->s1)) {
         temp=pop(q->s1);
         push(q->s2, temp);
      }}
   temp=pop(q->s2);
   return temp;
}



void myQueueFree(MyQueue* q) {
    freeStack(q->s1);
    freeStack(q->s2);
    free(q);
}

int main() {
    MyQueue* q = myQueueCreate();

    printf("Enqueuing 10, 20, 30...\n");
    myQueueEnqueue(q, 10);
    myQueueEnqueue(q, 20);
    myQueueEnqueue(q, 30);

    printf("Is queue empty? %s\n", myQueueIsEmpty(q) ? "true" : "false"); // Expected: false

    printf("Dequeuing: %d\n", myQueueDequeue(q)); // Expected: 10
    printf("Dequeuing: %d\n", myQueueDequeue(q)); // Expected: 20

    printf("Enqueuing 40...\n");
    myQueueEnqueue(q, 40);

    printf("Dequeuing: %d\n", myQueueDequeue(q)); // Expected: 30
    printf("Dequeuing: %d\n", myQueueDequeue(q)); // Expected: 40

    printf("Is queue empty? %s\n", myQueueIsEmpty(q) ? "true" : "false"); // Expected: true
    printf("Dequeuing: %d\n", myQueueDequeue(q)); // Expected: -1

    myQueueFree(q);
    return 0;
}