class MinStack:

    def __init__(self):
        self.s = []
        self.min_s = []

    def push(self, val: int) -> None:
        self.s.append(val)
        cur_min = min(val, self.min_s[-1] if self.min_s else val)
        self.min_s.append(cur_min)

    def pop(self) -> None:
        self.min_s.pop()
        return self.s.pop()

    def top(self) -> int:
        return self.s[-1]

    def getMin(self) -> int:
        return self.min_s[-1]