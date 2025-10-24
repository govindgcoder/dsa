#include <limits.h> // for INT_MAX
#include <stdio.h>

// A helper function for min, since C doesn't have one
int min(int a, int b) {
    return (a < b) ? a : b;
}

int minSubArrayLen(int target, int* nums, int numsSize) {
    // 1. Initialize your variables
    int left = 0;
    int currentSum = 0;
    int minLength = INT_MAX; // Use INT_MAX to mean "not found yet"
    int found = 0; // A flag to see if we ever find a valid window

    // 2. Loop 'right' pointer to expand the window
    for (int right = 0; right < numsSize; right++) {
        
        currentSum+=nums[right];

        // 4. Use a 'while' loop to shrink
        //    (Condition: while the window is valid...)
        while (currentSum>=target) {
            
            // 5. We found *a* valid window
            found = 1;
            
            // 6. Update the minLength
            minLength=minLength<right-left+1 ? minLength : right-left+1;
            
            // 7. Remove the 'left' element and shrink
            currentSum-=nums[left];
            left++;
        }
    }

    // 8. Return the final answer
    // (Handle the 'found = 0' case)
    return found ? minLength : 0;
}

// ------------------------------------------------------------------
// TEST HARNESS
// ------------------------------------------------------------------
int main() {
    int nums1[] = {2, 3, 1, 2, 4, 3};
    int size1 = 6;
    int target1 = 7;
    printf("Test 1 (Target: 7, Nums: [2, 3, 1, 2, 4, 3])\n");
    printf("Min Length: %d\n", minSubArrayLen(target1, nums1, size1)); // Expected: 2

    printf("\nTest 2 (Target: 4, Nums: [1, 4, 4])\n");
    int nums2[] = {1, 4, 4};
    int size2 = 3;
    int target2 = 4;
    printf("Min Length: %d\n", minSubArrayLen(target2, nums2, size2)); // Expected: 1

    printf("\nTest 3 (Target: 11, Nums: [1, 1, 1, 1, 1])\n");
    int nums3[] = {1, 1, 1, 1, 1};
    int size3 = 5;
    int target3 = 11;
    printf("Min Length: %d\n", minSubArrayLen(target3, nums3, size3)); // Expected: 0
    
    printf("\nTest 4 (Target: 15, Nums: [5, 1, 3, 5, 10, 7, 4, 9, 2, 8])\n");
    int nums4[] = {5, 1, 3, 5, 10, 7, 4, 9, 2, 8};
    int size4 = 10;
    int target4 = 15;
    printf("Min Length: %d\n", minSubArrayLen(target4, nums4, size4)); // Expected: 2

    return 0;
}
