class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        i, j = 0, 0
        result = []

        while i < len(firstList) and j < len(secondList):
            A = firstList[i]
            B = secondList[j]

            start = max(A[0], B[0])
            end = min(A[1], B[1])

            if start <= end:
                result.append([start, end])

            if A[1] < B[1]:
                i += 1
            else:
                j += 1

        return result


        