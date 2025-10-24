#include <stdio.h>
#include <stdlib.h>

// Helper to print
void printArray(int* arr, int size) {
    printf("[ ");
    for (int i = 0; i < size; i++) printf("%d ", arr[i]);
    printf("]\n");
}

// ------------------------------------------------------------------
// YOUR TASKS
// ------------------------------------------------------------------

// Task 1: Build the difference array
int* buildDifferenceArray(int* nums, int numsSize) {
    if (numsSize == 0) return NULL;
    int* diff = (int*)malloc(numsSize * sizeof(int));
    if (diff == NULL) return NULL;

    for(int i=0;i<numsSize;i++){
      diff[i]=i==0 ? nums[i] : nums[i]-nums[i-1];
    }

    return diff;
}

// Task 2: Update a range in O(1)
// Adds 'value' to all elements from 'left' to 'right' (inclusive)
void updateRange(int* diff, int numsSize, int left, int right, int value) {
    if(left<0||left>right||right>numsSize-1) return;
      diff[left]+=value;
    diff[right+1]-=value;
    return;
}

// Task 3: Rebuild the original array from the difference array
// This is just a prefix sum!
void rebuildArray(int* diff, int* nums, int numsSize) {
    if (numsSize == 0) return;

    for(int i=0;i<numsSize;i++){
      nums[i]= i==0 ? diff[i] : nums[i-1]+diff[i];
    }
}

// ------------------------------------------------------------------
// TEST HARNESS
// ------------------------------------------------------------------
int main() {
    int initial_nums[] = {10, 15, 12, 20, 18};
    int size = 5;

    printf("Original array: ");
    printArray(initial_nums, size);

    // 1. Build diff array
    int* diff = buildDifferenceArray(initial_nums, size);
    if (diff == NULL) return 1;
    printf("Difference array: ");
    printArray(diff, size); // Expected: [ 10 5 -3 8 -2 ]

    // 2. Perform updates
    printf("\nUpdating: Add 100 to range [1, 3]\n");
    updateRange(diff, size, 1, 3, 100);
    printf("Updated diff array: ");
    printArray(diff, size); // Expected: [ 10 105 -3 8 -102 ]
    
    printf("\nUpdating: Add -20 to range [0, 2]\n");
    updateRange(diff, size, 0, 2, -20);
    printf("Updated diff array: ");
    printArray(diff, size); // Expected: [ -10 105 -3 28 -102 ]

    // 3. Rebuild the final array
    // We'll rebuild it back into 'initial_nums'
    rebuildArray(diff, initial_nums, size);
    printf("\nRebuilt final array: ");
    printArray(initial_nums, size); // Expected: [ -10 95 92 120 18 ]
    
    free(diff);
    return 0;
}