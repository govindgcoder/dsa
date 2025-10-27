#include <stdio.h>

void printArray(int* arr, int size) {
    printf("[ ");
    for (int i = 0; i < size; i++) printf("%d ", arr[i]);
    printf("]\n");
}

// ------------------------------------------------------------------
// YOUR HELPER FUNCTION
// ------------------------------------------------------------------
void reverse(int* nums, int start, int end) {
    // A standard two-pointer reverse
    while (start < end) {
        // ... swap nums[start] and nums[end] ...
        // ... move pointers ...
    }
}

// ------------------------------------------------------------------
// YOUR MAIN FUNCTION
// ------------------------------------------------------------------
void rotate(int* nums, int numsSize, int k) {
    if (numsSize == 0) return;

    // 1. Handle the 'k > numsSize' edge case
    k = k % numsSize;
    
    if (k == 0) return; // No rotation needed

    // 2. Reverse the entire array (0 to numsSize - 1)
    
    // 3. Reverse the first 'k' elements (0 to k - 1)
    
    // 4. Reverse the remaining elements (k to numsSize - 1)
}

// ------------------------------------------------------------------
// TEST HARNESS
// ------------------------------------------------------------------
int main() {
    int nums1[] = {1, 2, 3, 4, 5, 6, 7};
    int size1 = 7;
    int k1 = 3;
    printf("Test 1 (Input: [1, 2, 3, 4, 5, 6, 7], k = 3)\n");
    rotate(nums1, size1, k1);
    printArray(nums1, size1); // Expected: [ 5 6 7 1 2 3 4 ]

    printf("\nTest 2 (Input: [-1, -100, 3, 99], k = 2)\n");
    int nums2[] = {-1, -100, 3, 99};
    int size2 = 4;
    int k2 = 2;
    rotate(nums2, size2, k2);
    printArray(nums2, size2); // Expected: [ 3 99 -1 -100 ]
    
    printf("\nTest 3 (Input: [1, 2], k = 5)\n");
    int nums3[] = {1, 2};
    int size3 = 2;
    int k3 = 5; // k > size, so k % size = 1
    rotate(nums3, size3, k3);
    printArray(nums3, size3); // Expected: [ 2 1 ]

    return 0;
}