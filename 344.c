#include <stdio.h>
#include <string.h> // For strlen()

void reverseString(char* s) {
    // 1. Find the length of the string (excluding the '\0')
    //    Or, initialize a 'right' pointer to the last *real* character.
    int n = strlen(s);
    int l=0;
    int r = n-1;
    char temp;
    while(l<r){
        temp=s[l];
        s[l]=s[r];
        s[r]=temp;
        l++; r--;
    }
}

// ------------------------------------------------------------------
// TEST HARNESS
// ------------------------------------------------------------------
int main() {
    char s1[] = "hello"; // The [] tells C to allocate 'h','e','l','l','o','\0'
    printf("Test 1 (Input: \"%s\")\n", s1);
    reverseString(s1);
    printf("Reversed: \"%s\"\n", s1); // Expected: "olleh"

    printf("\nTest 2 (Input: \"Hannah\")\n");
    char s2[] = "Hannah";
    reverseString(s2);
    printf("Reversed: \"%s\"\n", s2); // Expected: "hannaH"
    
    printf("\nTest 3 (Input: \"a\")\n");
    char s3[] = "a";
    reverseString(s3);
    printf("Reversed: \"%s\"\n", s3); // Expected: "a"
    
    printf("\nTest 4 (Input: \"\")\n");
    char s4[] = "";
    reverseString(s4);
    printf("Reversed: \"%s\"\n", s4); // Expected: ""
    
    return 0;
}