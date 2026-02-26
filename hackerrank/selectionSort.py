"""
Given an array arr, use selection sort to sort arr[] in increasing order.

Examples :
Input: arr[] = [4, 1, 3, 9, 7]
Output: [1, 3, 4, 7, 9]
Explanation: Maintain sorted (in bold) and unsorted subarrays. 
Select 1. Array becomes 1 4 3 9 7. Select 3. Array becomes 1 3 4 9 7. 
Select 4. Array becomes 1 3 4 9 7. Select 7. Array becomes 1 3 4 7 9. 
Select 9. Array becomes 1 3 4 7 9.

Input: arr[] = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

Input: arr[] = [38, 31, 20, 14, 30]
Output: [14, 20, 30, 31, 38]
"""

class Solution: 
    def selectionSort(self, arr):
        
        for i in range(len(arr)):
            min_dex = i
            for j in range(i+1, len(arr)):
                if arr[j] <= arr[min_dex]:
                    min_dex = j
            
            arr[i], arr[min_dex] = arr[min_dex], arr[i]

        print(arr)

if __name__ == '__main__':
    arr1 = [4, 1, 3, 9, 7]

    # names = ["Alice","Bob","Bob"]
    # heights = [155,185,150]

    Solution().selectionSort(arr1)