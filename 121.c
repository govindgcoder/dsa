#include <stdio.h>

int max(int a, int b) {
    return (a > b) ? a : b;
}

int min(int a, int b) {
    return (a < b) ? a : b;
   }

int maxProfit(int* prices, int pricesSize) {
    if (pricesSize < 2) {
        return 0; // Not enough days to buy and sell
    }

    int maxProfit = 0;
    int minPriceSoFar = prices[0];

    // Loop from the second day
    for (int i = 1; i < pricesSize; i++) {
        minPriceSoFar = min(minPriceSoFar, prices[i]);
        maxProfit = max(maxProfit, prices[i]-minPriceSoFar);
    }

    return maxProfit;
}

// ------------------------------------------------------------------
// TEST HARNESS
// ------------------------------------------------------------------
int main() {
    int prices1[] = {7, 1, 5, 3, 6, 4};
    int size1 = 6;
    printf("Test 1 (Input: [7, 1, 5, 3, 6, 4])\n");
    printf("Max Profit: %d\n", maxProfit(prices1, size1)); // Expected: 5

    printf("\nTest 2 (Input: [7, 6, 4, 3, 1])\n");
    int prices2[] = {7, 6, 4, 3, 1};
    int size2 = 5;
    printf("Max Profit: %d\n", maxProfit(prices2, size2)); // Expected: 0
    
    printf("\nTest 3 (Input: [2, 4, 1])\n");
    int prices3[] = {2, 4, 1};
    int size3 = 3;
    printf("Max Profit: %d\n", maxProfit(prices3, size3)); // Expected: 2

    return 0;
}