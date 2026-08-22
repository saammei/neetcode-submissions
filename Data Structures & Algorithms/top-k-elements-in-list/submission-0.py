class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        return heapq.nlargest(k, c.keys(), key=c.get)
