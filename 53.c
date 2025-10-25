#include <stdio.h>

int max(int a, int b) {
    return (a > b) ? a : b;
}

int maxSubArray(int* nums, int numsSize) {
    // 'Gotcha': You must initialize maxSum to the *first element*,
    // not 0. Why? What if the array is `[-5, -2, -3]`?
    // The correct answer is -2, but if you start maxSum at 0,
    // you'll get the wrong answer.
    if (numsSize == 0) return 0; // Edge case
    
    int maxSum = nums[0];
    int currentSum = nums[0];

    // 1. Loop from the *second* element onwards
    for (int i = 1; i < numsSize; i++) {
        
       currentSum = currentSum+nums[i]<nums[i] ? nums[i] : currentSum+nums[i];
       maxSum = max(maxSum, currentSum);
    }
    
    return maxSum;
}

// ------------------------------------------------------------------
// TEST HARNESS
// ------------------------------------------------------------------
int main() {
    int nums1[] = {1,2};
    int size1 = 2;
    printf("Test 1 (Input: [1,2])\n");
    printf("Max Sum: %d\n", maxSubArray(nums1, size1)); // Expected: 3

    printf("\nTest 2 (Input: [1])\n");
    int nums2[] = {1};
    int size2 = 1;
    printf("Max Sum: %d\n", maxSubArray(nums2, size2)); // Expected: 1

    printf("\nTest 3 (Input: [5, 4, -1, 7, 8])\n");
    int nums3[] = {5, 4, -1, 7, 8};
    int size3 = 5;
    printf("Max Sum: %d\n", maxSubArray(nums3, size3)); // Expected: 23
    
    printf("\nTest 4 (Input: [-5, -1, -3])\n");
    int nums4[] = {-5, -1, -3};
    int size4 = 3;
    printf("Max Sum: %d\n", maxSubArray(nums4, size4)); // Expected: -1

    return 0;
}