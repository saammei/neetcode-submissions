class MinStack:
        

    def __init__(self):
        self.data = []
        self.min = []

    def push(self, val: int) -> None:
        self.data.append(val)
        if not self.min or val <= self.min[-1]:
            self.min.append(val)

    def pop(self) -> None:
        x = self.data.pop()
        if x == self.min[-1]:
            self.min.pop()

    def top(self) -> int:
        return self.data[-1]
        
    def getMin(self) -> int:
        return self.min[-1]
