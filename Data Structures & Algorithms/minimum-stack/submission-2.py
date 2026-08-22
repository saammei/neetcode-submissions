class MinStack:

    def __init__(self):
        self.data = []
        self.min = []

    def push(self, val: int) -> None:
        self.data.append(val)
        cur_min = min(val, self.min[-1] if self.min else val)
        self.min.append(cur_min)

    def pop(self) -> None:
        self.data.pop()
        self.min.pop()

    def top(self) -> int:
        return self.data[-1]
        
    def getMin(self) -> int:
        return self.min[-1]
