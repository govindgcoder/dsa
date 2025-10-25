#include <stdio.h>

// Helper function for min
int min(int a, int b) {
    return (a < b) ? a : b;
}

// Helper function for max
int max(int a, int b) {
    return (a > b) ? a : b;
}

int maxArea(int* height, int heightSize) {
    int maxWater = 0;
    int currentWater;
    
    // 1. Initialize your two pointers
    int left = 0;
    int right = heightSize - 1;

    // 2. Loop until they meet
    while (left < right) {
        currentWater=(right-left)*min(height[left],height[right]);
        maxWater=max(maxWater, currentWater);
        if(height[left]<height[right]) left++;
        else right--;
    }

    return maxWater;
}

// ------------------------------------------------------------------
// TEST HARNESS
// ------------------------------------------------------------------
int main() {
    int height1[] = {1, 8, 6, 2, 5, 4, 8, 3, 7};
    int size1 = 9;
    printf("Test 1 (Input: [1, 8, 6, 2, 5, 4, 8, 3, 7])\n");
    printf("Max Area: %d\n", maxArea(height1, size1)); // Expected: 49

    printf("\nTest 2 (Input: [1, 1])\n");
    int height2[] = {1, 1};
    int size2 = 2;
    printf("Max Area: %d\n", maxArea(height2, size2)); // Expected: 1
    
    printf("\nTest 3 (Input: [4, 3, 2, 1, 4])\n");
    int height3[] = {4, 3, 2, 1, 4};
    int size3 = 5;
    printf("Max Area: %d\n", maxArea(height3, size3)); // Expected: 16

    printf("\nTest 4 (Input: [1, 2, 1])\n");
    int height4[] = {1, 2, 1};
    int size4 = 3;
    printf("Max Area: %d\n", maxArea(height4, size4)); // Expected: 2
    
    return 0;
}