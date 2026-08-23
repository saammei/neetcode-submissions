class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([timestamp, value])
        
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        nums = self.store[key]
        left, right = 0, len(nums)
        while left < right:
            mid = (left + right) // 2
            if timestamp >= nums[mid][0]:
                left = mid + 1
            else:
                right = mid
        return nums[left-1][1] if left > 0 else ""

