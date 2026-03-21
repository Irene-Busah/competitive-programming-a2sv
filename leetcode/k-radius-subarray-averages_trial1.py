class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        avgs = [-1] * n

        window_size = 2*k + 1
        if window_size > n:
            return avgs

        curr_sum = sum(nums[:window_size])

        for i in range(k, n - k):
            # compute average
            avgs[i] = curr_sum // window_size

            # slide window
            if i + k + 1 < n:
                curr_sum += nums[i + k + 1]
                curr_sum -= nums[i - k]

        return avgs