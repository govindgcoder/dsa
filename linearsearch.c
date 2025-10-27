#include <stdio.h>

// Your function here
int linearSearch(int* arr, int size, int target) {
    
    for(int i=0; i<size;i++){
        if(arr[i]==target) return i;
    }
    return -1;
}

int main() {
    int arr[] = {5, 2, 8, 12, 1, 6};
    int size = 6;
    
    printf("Searching for 12... Index: %d\n", linearSearch(arr, size, 12)); // Expected: 3
    printf("Searching for 7... Index: %d\n", linearSearch(arr, size, 7));   // Expected: -1
    return 0;
}