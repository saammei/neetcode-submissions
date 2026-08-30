class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        heapq.heapify(intervals)
        new_interval = heapq.heappop(intervals)
        res = []
        while len(intervals):
            curr_interval = heapq.heappop(intervals)
            if new_interval[1] < curr_interval[0]:
                res.append(new_interval)
                new_interval = curr_interval
            else:
                new_interval[1] = max(new_interval[1], curr_interval[1])
        res.append(new_interval)
        return res
