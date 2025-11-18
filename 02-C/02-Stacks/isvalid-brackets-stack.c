#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

#define MAX_SIZE 100 

typedef struct {
    char items[MAX_SIZE]; 
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

void push(Stack* s, char data) { 
    if (isFull(s)) {
        return; 
    }
    s->top++;
    s->items[s->top] = data;
}

char pop(Stack* s) { 
    if (isEmpty(s)) {
        return '\0'; 
    }
    char item = s->items[s->top];
    s->top--;
    return item;
}

char peek(Stack* s) { 
    if (isEmpty(s)) {
        return '\0';
    }
    return s->items[s->top];
}

void freeStack(Stack* s) {
    free(s);
}

bool isValid(char * s) {
   int i=0; char c;
   Stack *st = createStack();
   while(s[i]!='\0'){
      if(s[i]=='('||s[i]=='['||s[i]=='{') push(st,s[i]);
      else if(s[i]==')') {
         if(isEmpty(st)) return false;
         c=pop(st);
         if(c!='(') return false;
      } else if(s[i]==']') {
         if(isEmpty(st)) return false;
         c=pop(st);
         if(c!='[') return false;
      } else if(s[i]=='}') {
         if(isEmpty(st)) return false;
         c=pop(st);
         if(c!='{') return false;
      }
      i++;
   }
   return isEmpty(st) ? true : false;
}

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
