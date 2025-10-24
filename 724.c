#include <stdio.h>

int pivotIndex(int* nums, int numsSize) {
    if (numsSize == 0) return -1;

    // 1. --- Pass 1: Calculate totalSum ---
    int totalSum = 0;
    // ... your for-loop to calculate totalSum ...
   for(int i=0;i<numsSize;i++){
      totalSum+=nums[i];
   }

    // 2. --- Pass 2: Find the pivot ---
    int leftSum = 0; int rightSum;
    for (int i = 0; i < numsSize; i++) {
         leftSum += i==0 ? 0: nums[i-1];
         rightSum = totalSum-(leftSum+nums[i]);
         if(rightSum==leftSum) return i; 
    }

    // 6. --- No pivot found ---
    return -1;
}

// ------------------------------------------------------------------
// TEST HARNESS
// ------------------------------------------------------------------
int main() {
    int nums1[] = {1, 7, 3, 6, 5, 6};
    int size1 = 6;
    printf("Test 1 (Input: [1, 7, 3, 6, 5, 6])\n");
    printf("Pivot Index: %d\n", pivotIndex(nums1, size1)); // Expected: 3

    printf("\nTest 2 (Input: [1, 2, 3])\n");
    int nums2[] = {1, 2, 3};
    int size2 = 3;
    printf("Pivot Index: %d\n", pivotIndex(nums2, size2)); // Expected: -1

    printf("\nTest 3 (Input: [2, 1, -1])\n");
    int nums3[] = {2, 1, -1};
    int size3 = 3;
    printf("Pivot Index: %d\n", pivotIndex(nums3, size3)); // Expected: 0
    // (At index 0: leftSum = 0, rightSum = 1 + (-1) = 0)

    printf("\nTest 4 (Input: [-1, -1, 0, 1, 1, 0])\n");
    int nums4[] = {-1, -1, 0, 1, 1, 0};
    int size4 = 6;
    printf("Pivot Index: %d\n", pivotIndex(nums4, size4)); // Expected: 5

    return 0;
}