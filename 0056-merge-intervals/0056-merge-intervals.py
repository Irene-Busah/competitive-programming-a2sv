class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sorted_array = sorted(intervals, key=lambda x: x[0])
        interval = []

        cur_start, cur_end = sorted_array[0]

        for start, end in sorted_array[1:]:
            
            if start <= cur_end:
                cur_end = max(cur_end, end)
            else:
                interval.append([cur_start, cur_end])
                cur_start, cur_end = start, end
            
        interval.append([cur_start, cur_end])
        return interval