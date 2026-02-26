class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:

        res = []

        for n in range(len(arr), 1, -1):
            i = arr.index(n)

            if i == n - 1:  # already in correct position
                continue

            if i != 0:
                res.append(i + 1)
                arr[:i + 1] = reversed(arr[:i + 1])  # bring n to front

            res.append(n)
            arr[:n] = reversed(arr[:n])  # move n to position n-1

        return res

        