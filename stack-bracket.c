#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

// ------------------------------------------------------------------
// COPY/PASTE YOUR STACK IMPLEMENTATION (struct + functions) HERE
// ------------------------------------------------------------------

#define MAX_SIZE 100 

typedef struct {
    char items[MAX_SIZE]; // Make this a 'char' stack!
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

void push(Stack* s, char data) { // 'char' data
    if (isFull(s)) {
        return; // Fail silently for this problem
    }
    s->top++;
    s->items[s->top] = data;
}

char pop(Stack* s) { // 'char' data
    if (isEmpty(s)) {
        return '\0'; // Return null char on underflow
    }
    char item = s->items[s->top];
    s->top--;
    return item;
}

char peek(Stack* s) { // 'char' data
    if (isEmpty(s)) {
        return '\0';
    }
    return s->items[s->top];
}

void freeStack(Stack* s) {
    free(s);
}

// ------------------------------------------------------------------

// YOUR FUNCTION GOES HERE
bool isValid(char * s) {
    // Your implementation here
    return false; // Placeholder
}

// ------------------------------------------------------------------
// TEST HARNESS
// ------------------------------------------------------------------
int main() {
    char* s1 = "()";
    printf("Test 1 (\"%s\"): %s\n", s1, isValid(s1) ? "true" : "false"); // Expected: true

    char* s2 = "()[]{}";
    printf("Test 2 (\"%s\"): %s\n", s2, isValid(s2) ? "true" : "false"); // Expected: true

    char* s3 = "(]";
    printf("Test 3 (\"%s\"): %s\n", s3, isValid(s3) ? "true" : "false"); // Expected: false

    char* s4 = "([)]";
    printf("Test 4 (\"%s\"): %s\n", s4, isValid(s4) ? "true" : "false"); // Expected: false

    char* s5 = "{[]}";
    printf("Test 5 (\"%s\"): %s\n", s5, isValid(s5) ? "true" : "false"); // Expected: true

    char* s6 = "(";
    printf("Test 6 (\"%s\"): %s\n", s6, isValid(s6) ? "true" : "false"); // Expected: false

    char* s7 = ")";
    printf("Test 7 (\"%s\"): %s\n", s7, isValid(s7) ? "true" : "false"); // Expected: false
    
    return 0;
}
