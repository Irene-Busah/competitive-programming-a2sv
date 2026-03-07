class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """

        numZeros = arr.count(0)

        left, right = len(arr) - 1, len(arr) + numZeros - 1

        while left >= 0:
            if right < len(arr):
                arr[right] = arr[left]

            if arr[left] == 0:
                right -= 1
                if right < len(arr):
                    arr[right] = 0
            
            left -= 1
            right -= 1
        